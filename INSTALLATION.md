# 📄 INSTALLATION.md  
Guide d’installation — HuggingFace‑CATAR  
Version 1.0 — Simulation locale et utilisation libre

---

## 01 — Prérequis

- **Système recommandé** : Ubuntu ≥ 22.04  
- **Python** : version ≥ 3.10  
- **Git** : pour cloner le dépôt  
- **Cargo/Rust** : uniquement si vous souhaitez compiler Subtensor (optionnel, pour intégration réseau)  

---

## 02 — Cloner le dépôt

```bash
git clone https://github.com/QuatreCATAR/HuggingFace-CATAR.git
cd HuggingFace-CATAR
```

03 — Installer les dépendances Python
bash
pip install -r requirements.txt

04 — Lancer l’application en simulation locale
Miner (production de réponses conceptuelles)
bash
python3 miners/miner.py
Validator (évaluation et stabilisation)
bash
python3 validators/validator.py
Ces deux modules fonctionnent en simulation locale et permettent de tester la logique du Passage CATAR sans interaction externe.
Ils peuvent être adaptés pour des environnements distribués.

05 — Tests
Des tests unitaires sont disponibles dans le dossier tests/.
Ils permettent de vérifier :

la cohérence des transmissions,

la stabilité des interactions locales,

la reproductibilité des résultats.

Exécution des tests :

bash
pytest tests/

06 — Documentation complémentaire
[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !] — présentation générale

[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !] — guide développeur détaillé

[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !] — feuille de route

[Il semble que le résultat n’était pas sûr à afficher. Changeons un peu et essayons autre chose !] — règles de contribution
