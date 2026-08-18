import time
from typing import Tuple
import argparse
import logging
import bittensor as bt
import yaml
import os
import sys

# Passage CATAR (Corpus public mais non-modifiable)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'catar_core')))
from passage_catar import PassageCATAR

# Synapse CATAR
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'synapses')))
from synapse_catar import SynapseCATAR


# === Callbacks ===

def blacklist_fn(synapse: SynapseCATAR) -> Tuple[bool, str]:
    """
    Fonction de filtrage des requêtes entrantes.
    Pour l'instant, on accepte toutes les requêtes.
    """
    return (False, "Accepted")


def priority_fn(synapse: SynapseCATAR) -> float:
    """
    Fonction de priorité des requêtes entrantes.
    Pour l'instant, toutes les requêtes ont la même priorité.
    """
    return 0.5


# === Configuration ===

def load_settings():
    settings_path = os.path.join("config", "settings.yaml")
    with open(settings_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_config():
    parser = argparse.ArgumentParser()
    bt.Axon.add_args(parser)
    bt.Wallet.add_args(parser)
    bt.Subtensor.add_args(parser)
    bt.logging.add_args(parser)

    config = bt.Config(parser)
    bt.logging(config=config, logging_dir="logs/miner")

    return config


# === Classe principale ===

class MinerCATAR:
    def __init__(self, config: bt.Config):
        self.config = config
        self.settings = load_settings()

        # Passage CATAR : lit le Corpus, ne le modifie jamais
        self.passage = PassageCATAR()

        # Wallet / Subtensor
        self.wallet = bt.Wallet(config=self.config)
        self.subtensor = bt.Subtensor(config=self.config)

        # Axon : point d'entrée réseau du miner
        self.axon = bt.Axon(
            wallet=self.wallet,
            config=self.config,
            port=self.settings["miner"]["axon_port"],
        )

        # Attache des callbacks (version compatible avec ta version de Bittensor)
        self.axon.attach(
            forward_fn=self.forward,
            blacklist_fn=blacklist_fn,
            priority_fn=priority_fn,
        )

        bt.logging.info("MinerCATAR initialisé avec settings.yaml.")

    def forward(self, synapse: SynapseCATAR) -> SynapseCATAR:
        """
        Reçoit un SynapseCATAR, applique PassageCATAR, renvoie un SynapseCATAR.
        Le Corpus brut n'est jamais renvoyé.
        """
        prompt = synapse.prompt or "Entrée CATAR par défaut"

        result = self.passage.execute(
            test_input=prompt,
            corpus_path=self.settings["catar"]["corpus_path"],
        )

        synapse.test = result["test"]
        synapse.control = result["control"]
        synapse.correction = result["correction"]
        synapse.analysis = result["analysis"]

        bt.logging.info("Passage CATAR exécuté avec succès.")
        return synapse

    def run(self):
        bt.logging.info("Démarrage du miner CATAR...")
        self.axon.start()
        bt.logging.info("MinerCATAR actif. Ctrl+C pour arrêter.")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            bt.logging.info("Arrêt du miner CATAR.")
            self.axon.stop()


# === Main ===

if __name__ == "__main__":
    config = get_config()
    miner = MinerCATAR(config)
    miner.run()
    print("=== MinerCATAR initialisé et prêt ===")

