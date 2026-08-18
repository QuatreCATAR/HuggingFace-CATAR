import time
import argparse
import logging
import bittensor as bt
import yaml
import os
from pathlib import Path
import sys

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

logging.basicConfig(
    filename="logs/validator/validator.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def load_settings():
    settings_path = os.path.join("config", "settings.yaml")
    with open(settings_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def get_config():
    parser = argparse.ArgumentParser()
    bt.Wallet.add_args(parser)
    bt.Subtensor.add_args(parser)
    bt.logging.add_args(parser)

    config = bt.Config(parser)
    bt.logging(config=config, logging_dir="logs/validator")

    return config

class ValidatorCATAR:
    def __init__(self, config: bt.Config):
        self.config = config
        self.settings = load_settings()

        # Wallet / Subtensor / Dendrite
        self.wallet = bt.Wallet(name="catar_validator", hotkey="catar_validator")
        self.subtensor = bt.Subtensor(config=self.config)
        self.dendrite = bt.Dendrite(wallet=self.wallet)

        logging.info("ValidatorCATAR initialisé (réseau).")

    def query_miner(self, prompt: str) -> dict:
        synapse = SynapseCATAR(prompt=prompt)

        axons = self.subtensor.neurons(self.config.netuid)
        if not axons:
            logging.warning("Aucun axon trouvé sur le subnet CATAR.")
            return {}

        response = self.dendrite.forward(
            synapse=synapse,
            axons=[axons[0]],
        )

        return response.to_dict()

    def score_presence(self, miner_output):
        return sum(SECTION_WEIGHTS[k] for k in SECTION_WEIGHTS if k in miner_output)

    def score_coherence(self, miner_output):
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

    def score_semantic(self, miner_output):
        from difflib import SequenceMatcher

        corpus = miner_output.get("Corpus", "")
        analysis = miner_output.get("Analysis", "")

        if not corpus or not analysis:
            return 0

        return SequenceMatcher(None, corpus, analysis).ratio()

    def compute_catar_score(self, miner_output):
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
        logging.info("Démarrage du validator CATAR (réseau)...")

        try:
            while True:
                miner_output = self.query_miner("Test CATAR depuis le validator")

                if not miner_output:
                    logging.warning("Aucune réponse du miner.")
                    time.sleep(2)
                    continue

                scores = self.compute_catar_score(miner_output)

                logging.info(f"Score CATAR final = {scores['final_score']:.2f}")
                logging.info(f"Détails du score : {scores}")
                logging.debug(miner_output)

                time.sleep(2)

        except KeyboardInterrupt:
            logging.info("Arrêt du validator CATAR.")
            print("Arrêt du validator CATAR.")

def main():
    config = get_config()
    validator = ValidatorCATAR(config=config)
    validator.run()

if __name__ == "__main__":
    main()
