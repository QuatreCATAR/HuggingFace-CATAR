# compte_rendu.py
# Module de génération du Compte-Rendu CATAR

import logging
from datetime import datetime

# -----------------------------------------------------------------------------
# 01 — Classe CompteRenduCATAR
# -----------------------------------------------------------------------------

class CompteRenduCATAR:
    """
    Génère un Compte-Rendu CATAR structuré à partir :
    - du Passage CATAR
    - de la Correction réelle
    - de l’Analyse CATAR
    - du score global
    """

    def __init__(self):
        logging.info("CompteRenduCATAR initialisé.")

    # -------------------------------------------------------------------------
    # 02 — Génération du rapport CATAR
    # -------------------------------------------------------------------------

    def generate(self, passage_result: dict, correction_result: dict, analysis_result: dict):
        """
        Génère un rapport CATAR structuré.
        """

        score_correction = correction_result.get("score", 0.0)
        score_analyse = analysis_result.get("score", 0.0)
        score_global = score_correction + score_analyse

        invariants = correction_result.get("markers", [])
        moije_soije = analysis_result.get("moije_soije", "")
        absolu_relatif = analysis_result.get("absolu_relatif", "")
        dphi = analysis_result.get("dphi", "")

        # Date du passage
        date_passage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ---------------------------------------------------------------------
        # 03 — Construction du Compte-Rendu (format Markdown)
        # ---------------------------------------------------------------------

        compte_rendu = f"""
# Compte-Rendu CATAR
Date : {date_passage}

---

## 01 — Résultats du Passage CATAR

### Test
{passage_result.get("test")}

### Corpus utilisé
{passage_result.get("corpus")}

### Contrôle
{passage_result.get("control")}

### Correction
{passage_result.get("correction")}

### Analyse
{passage_result.get("analysis")}

---

## 02 — Correction CATAR (réelle)

### Score de correction
**{score_correction} / 5**

### Invariants détectés
{", ".join(invariants) if invariants else "Aucun invariant détecté"}

---

## 03 — Analyse CATAR (réelle)

### Score d’analyse
**{score_analyse} / 3**

### Moije / Soije
{moije_soije}

### Absolu / Relatif
{absolu_relatif}

### D.Phi
{dphi}

---

## 04 — Score global CATAR

### Score total
**{score_global} / 8**

---

## 05 — Diagnostic CATAR

- Cohérence conceptuelle : {moije_soije}
- Structure Absolu/Relatif : {absolu_relatif}
- Présence hermétique (D.Phi) : {dphi}
- Invariants détectés : {", ".join(invariants) if invariants else "aucun"}

---

## 06 — Conclusion

Le Passage CATAR a été exécuté, corrigé et analysé.
Le score global reflète :
- la stabilité conceptuelle,
- la cohérence hermétique,
- l’intégration des invariants CATAR.

---

## 07 — Données brutes (debug)

### Passage
{passage_result}

### Correction
{correction_result}

### Analyse
{analysis_result}

---

# Fin du Compte-Rendu CATAR
"""

        logging.info("Compte-Rendu CATAR généré.")
        return compte_rendu


# -----------------------------------------------------------------------------
# 08 — Exemple d’utilisation
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # Exemple minimal
    passage = {
        "test": "Entrée de test",
        "corpus": "Corpus chargé",
        "control": "Contrôle OK",
        "correction": "Correction OK",
        "analysis": "Analyse OK"
    }

    correction = {
        "score": 3.0,
        "markers": ["Moije", "Soije"],
        "raw_output": "Moije Soije Absolu",
        "correction_reference": "..."
    }

    analyse = {
        "score": 2.0,
        "moije_soije": "Moije/Soije équilibrés",
        "absolu_relatif": "Absolu/Relatif équilibrés",
        "dphi": "D.Phi détecté"
    }

    cr = CompteRenduCATAR()
    print(cr.generate(passage, correction, analyse))
