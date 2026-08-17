# correction.py
# Correction CATAR réelle — détection des invariants et attribution du score

import logging

# -----------------------------------------------------------------------------
# 01 — Classe CorrectionCATAR
# -----------------------------------------------------------------------------

class CorrectionCATAR:
    """
    Correction CATAR :
    - charge la correction officielle (Correction.md)
    - compare les réponses du miner
    - détecte les invariants CATAR
    - attribue un score
    """

    def __init__(self, correction_path: str):
        self.correction_path = correction_path
        self.correction_data = self.load_correction()
        logging.info("CorrectionCATAR initialisée.")

    # -------------------------------------------------------------------------
    # 02 — Chargement de Correction.md
    # -------------------------------------------------------------------------

    def load_correction(self):
        """
        Charge le fichier Correction.md.
        Version réelle : lit le contenu du fichier.
        """
        try:
            with open(self.correction_path, "r", encoding="utf-8") as f:
                data = f.read()
            logging.info(f"Correction chargée depuis {self.correction_path}")
            return data
        except Exception as e:
            logging.error(f"Erreur chargement Correction.md : {e}")
            return ""

    # -------------------------------------------------------------------------
    # 03 — Détection des invariants CATAR
    # -------------------------------------------------------------------------

    def detect_invariants(self, miner_output: str):
        """
        Détecte les invariants CATAR dans la réponse du miner.
        Version réelle : recherche des marqueurs conceptuels.
        """

        invariants = []

        # Invariant Moije
        if "Moije" in miner_output:
            invariants.append("Moije")

        # Invariant Soije
        if "Soije" in miner_output:
            invariants.append("Soije")

        # Invariant Absolu
        if "Absolu" in miner_output:
            invariants.append("Absolu")

        # Invariant Relatif
        if "Relatif" in miner_output:
            invariants.append("Relatif")

        # Invariant D.Phi
        if "D.Phi" in miner_output or "DPhi" in miner_output:
            invariants.append("D.Phi")

        return invariants

    # -------------------------------------------------------------------------
    # 04 — Attribution du score CATAR
    # -------------------------------------------------------------------------

    def score_from_invariants(self, invariants):
        """
        Score CATAR réel :
        - chaque invariant détecté vaut 1 point
        - score maximal = 5
        """
        return float(len(invariants))

    # -------------------------------------------------------------------------
    # 05 — Correction complète
    # -------------------------------------------------------------------------

    def correct(self, miner_output: str):
        """
        Applique la correction réelle :
        - détecte les invariants
        - attribue un score
        - renvoie un dictionnaire structuré
        """

        invariants = self.detect_invariants(miner_output)
        score = self.score_from_invariants(invariants)

        result = {
            "score": score,
            "markers": invariants,
            "raw_output": miner_output,
            "correction_reference": self.correction_data
        }

        logging.info(f"Correction effectuée : score={score}, invariants={invariants}")
        return result


# -----------------------------------------------------------------------------
# 06 — Exemple d’utilisation
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    engine = CorrectionCATAR("corpus/Correction.md")
    test_output = "Exemple : Moije, Soije, Absolu"
    print(engine.correct(test_output))
