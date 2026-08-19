import time
import argparse
import logging
import json
import bittensor as bt
import yaml
import os
from pathlib import Path
import sys
from typing import Dict

# Synapse CATAR
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'synapses')))
from synapse_catar import SynapseCATAR

SECTION_WEIGHTS = {
    "Corpus": 3,
    "Control": 2,
    "Correction": 2,
    "Analysis": 3,
    "test": 1,
}

# === Logging configuration ===
logging.basicConfig(
    filename="logs/validator/validator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# === Settings loader ===
def load_settings() -> Dict:
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

# === Config parser ===
def get_config():
    parser = argparse.ArgumentParser(description="ValidatorCATAR execution")
    parser.add_argument("--iterations", type=int, default=0,
                        help="Number of iterations before stopping (0 = infinite)")
    parser.add_argument("--output", type=str, default="",
                        help="Optional path to save structured outputs (JSON)")
    bt.Wallet.add_args(parser)
    bt.Subtensor.add_args(parser)
    bt.logging.add_args(parser)

    config = bt.Config(parser)
    bt.logging(config=config, logging_dir="logs/validator")

    return config

# === Main Validator Class ===
class ValidatorCATAR:
    def __init__(self, config: bt.Config, iterations: int = 0, output: str = ""):
        self.config = config
        self.settings = load_settings()
        self.iterations = iterations
        self.output = output

        # Wallet / Subtensor / Dendrite
        self.wallet = bt.Wallet(name="catar_validator", hotkey="catar_validator")
        self.subtensor = bt.Subtensor(config=self.config)
        self.dendrite = bt.Dendrite(wallet=self.wallet)

        logging.info("ValidatorCATAR initialized (network).")

    def query_miner(self, prompt: str) -> dict:
        """
        Send a SynapseCATAR to a miner and return its output.
        """
        synapse = SynapseCATAR(prompt=prompt)
        try:
            axons = self.subtensor.neurons(self.config.netuid)
            if not axons:
                logging.warning("No axon found on CATAR subnet.")
                return {}

            response = self.dendrite.forward(
                synapse=synapse,
                axons=[axons[0]],
            )
            return response.to_dict()
        except Exception as e:
            logging.error(f"Error querying miner: {e}")
            return {}

    def score_presence(self, miner_output: dict) -> int:
        return sum(SECTION_WEIGHTS[k] for k in SECTION_WEIGHTS if k in miner_output)

    def score_coherence(self, miner_output: dict) -> int:
        coherence = 0
        corpus = miner_output.get("Corpus", "")
        analysis = miner_output.get("Analysis", "")
        correction = miner_output.get("Correction", "")
        control = miner_output.get("Control", "")

        if corpus and analysis and corpus[:20] in analysis:
            coherence += 2
        if correction and corpus and len(correction) > len(corpus):
            coherence += 2
        if control and "cohérent" in control.lower():
            coherence += 2

        return coherence

    def score_semantic(self, miner_output: dict) -> float:
        from difflib import SequenceMatcher
        corpus = miner_output.get("Corpus", "")
        analysis = miner_output.get("Analysis", "")
        if not corpus or not analysis:
            return 0.0
        return SequenceMatcher(None, corpus, analysis).ratio()

    def compute_catar_score(self, miner_output: dict) -> dict:
        presence = self.score_presence(miner_output)
        coherence = self.score_coherence(miner_output)
        semantic = self.score_semantic(miner_output)

        final_score = (presence * 0.5) + (coherence * 0.3) + (semantic * 0.2)

        return {
            "presence_score": presence,
            "coherence_score": coherence,
            "semantic_score": semantic,
            "final_score": final_score,
        }

    def run(self):
        """
        Main loop: query miner, compute scores, log results.
        """
        logging.info("Starting ValidatorCATAR (network)...")
        try:
            count = 0
            while True:
                miner_output = self.query_miner("CATAR test from validator")

                if not miner_output:
                    logging.warning("No response from miner.")
                    time.sleep(2)
                    continue

                scores = self.compute_catar_score(miner_output)

                logging.info(f"Final CATAR score = {scores['final_score']:.2f}")
                logging.info(f"Score details: {scores}")
                logging.debug(miner_output)

                # Optional structured output
                if self.output:
                    with open(self.output, "a", encoding="utf-8") as f:
                        f.write(json.dumps(scores, ensure_ascii=False) + "\n")

                time.sleep(2)

                if self.iterations > 0:
                    count += 1
                    if count >= self.iterations:
                        logging.info("Stopping ValidatorCATAR after iterations limit.")
                        break

        except KeyboardInterrupt:
            logging.info("ValidatorCATAR stopped manually.")
            print("ValidatorCATAR stopped.")

# === Main ===
def main():
    config = get_config()
    validator = ValidatorCATAR(config=config,
                               iterations=config.get("iterations", 0),
                               output=config.get("output", ""))
    validator.run()

if __name__ == "__main__":
    main()
