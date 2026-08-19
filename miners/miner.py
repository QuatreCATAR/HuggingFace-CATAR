import time
import argparse
import logging
import json
import bittensor as bt
import yaml
import os
import sys
from typing import Tuple

# Passage CATAR (Corpus public mais non-modifiable)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'catar_core')))
from passage_catar import PassageCATAR

# Synapse CATAR
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'synapses')))
from synapse_catar import SynapseCATAR


# === Callbacks ===

def blacklist_fn(synapse: SynapseCATAR) -> Tuple[bool, str]:
    """
    Filtering function for incoming requests.
    Currently accepts all requests.
    """
    return (False, "Accepted")


def priority_fn(synapse: SynapseCATAR) -> float:
    """
    Priority function for incoming requests.
    Currently all requests have equal priority.
    """
    return 0.5


# === Configuration ===

def load_settings():
    """
    Load miner settings from config/settings.yaml.
    """
    settings_path = os.path.join("config", "settings.yaml")
    try:
        with open(settings_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.error("settings.yaml not found in config/.")
        return {}
    except yaml.YAMLError as e:
        logging.error(f"Error parsing settings.yaml: {e}")
        return {}


def get_config():
    """
    Parse CLI arguments and initialize Bittensor config.
    """
    parser = argparse.ArgumentParser(description="MinerCATAR execution")
    parser.add_argument("--iterations", type=int, default=0,
                        help="Number of iterations before stopping (0 = infinite)")
    parser.add_argument("--output", type=str, default="",
                        help="Optional path to save structured outputs (JSON)")
    bt.Axon.add_args(parser)
    bt.Wallet.add_args(parser)
    bt.Subtensor.add_args(parser)
    bt.logging.add_args(parser)

    config = bt.Config(parser)
    bt.logging(config=config, logging_dir="logs/miner")

    return config


# === Main Miner Class ===

class MinerCATAR:
    def __init__(self, config: bt.Config, iterations: int = 0, output: str = ""):
        self.config = config
        self.settings = load_settings()
        self.iterations = iterations
        self.output = output

        # Passage CATAR : reads Corpus, never modifies it
        self.passage = PassageCATAR()

        # Wallet / Subtensor
        self.wallet = bt.Wallet(config=self.config)
        self.subtensor = bt.Subtensor(config=self.config)

        # Axon : network entry point of the miner
        self.axon = bt.Axon(
            wallet=self.wallet,
            config=self.config,
            port=self.settings.get("miner", {}).get("axon_port", 8091),
        )

        # Attach callbacks
        self.axon.attach(
            forward_fn=self.forward,
            blacklist_fn=blacklist_fn,
            priority_fn=priority_fn,
        )

        logging.info("MinerCATAR initialized with settings.yaml.")

    def forward(self, synapse: SynapseCATAR) -> SynapseCATAR:
        """
        Receives a SynapseCATAR, applies PassageCATAR, returns a SynapseCATAR.
        The raw Corpus is never returned.
        """
        prompt = synapse.prompt or "Default CATAR input"
        try:
            result = self.passage.execute(
                test_input=prompt,
                corpus_path=self.settings.get("catar", {}).get("corpus_path", ""),
            )

            synapse.test = result.get("test", "")
            synapse.control = result.get("control", "")
            synapse.correction = result.get("correction", "")
            synapse.analysis = result.get("analysis", "")

            logging.info("PassageCATAR executed successfully.")

            # Optional structured output
            if self.output:
                with open(self.output, "a", encoding="utf-8") as f:
                    f.write(json.dumps(result, ensure_ascii=False) + "\n")

        except Exception as e:
            logging.error(f"Error in forward execution: {e}")

        return synapse

    def run(self):
        """
        Run the miner loop.
        """
        logging.info("Starting MinerCATAR...")
        self.axon.start()
        logging.info("MinerCATAR active. Ctrl+C to stop.")

        try:
            count = 0
            while True:
                time.sleep(1)
                if self.iterations > 0:
                    count += 1
                    if count >= self.iterations:
                        logging.info("Stopping MinerCATAR after iterations limit.")
                        break
        except KeyboardInterrupt:
            logging.info("MinerCATAR stopped manually.")
        finally:
            self.axon.stop()


# === Main ===

if __name__ == "__main__":
    config = get_config()
    miner = MinerCATAR(config, iterations=config.get("iterations", 0),
                       output=config.get("output", ""))
    miner.run()
    print("=== MinerCATAR initialized and ready ===")
