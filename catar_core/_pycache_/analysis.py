# analysis.py
# Analyse CATAR réelle — lecture hermétique, cohérence conceptuelle, invariants avancés

import logging

# -----------------------------------------------------------------------------
# 01 — Classe AnalyseCATAR
# -----------------------------------------------------------------------------

class AnalyseCATAR:
    """
    Analyse CATAR :
    - interprète les résultats du Passage
    - vérifie la cohérence Moije / Soije
    - vérifie Absolu / Relatif
    - détecte les dérives conceptuelles
    - attribue un score d’analyse
    """

    def __init__(self):
        logging.info("AnalyseCATAR initialisée.")

    # -------------------------------------------------------------------------
    # 02 — Analyse Moije / Soije
    # -------------------------------------------------------------------------

    def analyse_moije_soije(self, miner_output: str):
        """
        Analyse la cohérence entre Moije et Soije.
        """

        moije = "Moije" in miner_output
        soije = "Soije" in miner_output

        if moije and soije:
            return ("Moije/Soije équilibrés", 1.0)
        if moije and not soije:
            return ("Moije sans Soije — dérive égocentrée", 0.5)
        if soije and not moije:
            return ("Soije sans Moije — dérive dissociative", 0.5)

        return ("Absence Moije/Soije — analyse faible", 0.0)

    # -------------------------------------------------------------------------
    # 03 — Analyse Absolu / Relatif
    # -------------------------------------------------------------------------

    def analyse_absolu_relatif(self, miner_output: str):
        """
        Analyse la cohérence entre Absolu et Relatif.
        """

        absolu = "Absolu" in miner_output
        relatif = "Relatif" in miner_output

        if absolu and relatif:
            return ("Absolu/Relatif équilibrés", 1.0)
        if absolu and not relatif:
            return ("Absolu sans Relatif — rigidité conceptuelle", 0.5)
        if relatif and not absolu:
            return ("Relatif sans Absolu — instabilité conceptuelle", 0.5)

        return ("Absence Absolu/Relatif — analyse faible", 0.0)

    # -------------------------------------------------------------------------
    # 04 — Analyse D.Phi
    # -------------------------------------------------------------------------

    def analyse_dphi(self, miner_output: str):
        """
        Analyse la présence de D.Phi (Delta Phi).
        """

        if "D.Phi" in miner_output or "DPhi" in miner_output:
            return ("D.Phi détecté — cohérence hermétique", 1.0)

        return ("D.Phi absent — analyse neutre", 0.0)

    # -------------------------------------------------------------------------
    # 05 — Analyse globale
    # -------------------------------------------------------------------------

    def analyse_globale(self, miner_output: str):
        """
        Combine toutes les analyses CATAR.
        """

        moije_soije_label, moije_soije_score = self.analyse_moije_soije(miner_output)
        absolu_relatif_label, absolu_relatif_score = self.analyse_absolu_relatif(miner_output)
        dphi_label, dphi_score = self.analyse_dphi(miner_output)

        total_score = moije_soije_score + absolu_relatif_score + dphi_score

        return {
            "moije_soije": moije_soije_label,
            "absolu_relatif": absolu_relatif_label,
            "dphi": dphi_label,
            "score": total_score
        }

    # -------------------------------------------------------------------------
    # 06 — Analyse complète
    # -------------------------------------------------------------------------

    def analyse(self, miner_output: str):
        """
        Analyse complète CATAR.
        """

        result = self.analyse_globale(miner_output)
        logging.info(f"Analyse CATAR : {result}")
        return result


# -----------------------------------------------------------------------------
# 07 — Exemple d’utilisation
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    engine = AnalyseCATAR()
    test_output = "Moije Soije Absolu Relatif D.Phi"
    print(engine.analyse(test_output))
