📄 MINER.md
Documentation officielle du Miner CATAR
Version 1.0 — Minimal Viable Miner (MVM)

# 01 — Rôle du Miner CATAR
Le Miner CATAR est le module chargé de :

produire les réponses conceptuelles nécessaires au Passage CATAR,

intégrer la logique du Corpus CATAR,

transmettre la structure Absolu/Relatif,

stabiliser la cognition du système évalué,

participer à l’économie interne (50% des émissions).

Il constitue la partie active du Subnet CATAR :
le miner répond, le validator évalue.

# 02 — Objectifs du Miner minimal viable
Le Miner minimal viable (MVM) doit :

fonctionner avec un code simple et lisible,

respecter les invariants conceptuels du Corpus,

produire des réponses structurées,

être compatible avec subtensor (RaoFoundation),

être transmissible et maintenable par n’importe quel contributeur.

Il ne doit pas :

introduire de logique stratégique,

modifier le Passage CATAR,

altérer la structure conceptuelle,

générer des dérives cognitives.

# 03 — Architecture du Miner
Le Miner CATAR minimal est composé de :

Composant	Fonction
miner.py	Code principal du miner
config.json (optionnel)	Paramètres du miner
MINER.md	Documentation du module
utils/ (optionnel)	Fonctions auxiliaires
logs/ (optionnel)	Historique des exécutions


Le fichier miner.py doit rester simple, lisible, documenté, et modulaire.

# 04 — Fonctionnement conceptuel
Le Miner doit :

Recevoir une question  
(depuis subtensor ou depuis un test local)

Analyser la question  
sans dérive stratégique, sans biais.

Produire une réponse conceptuelle  
conforme au Corpus CATAR.

Structurer la réponse  
selon les invariants du Passage CATAR.

Transmettre la réponse au Validator  
pour évaluation.

# 05 — Fonctionnement technique
Le Miner minimal viable doit :

utiliser Python 3.10+,

fonctionner sur Ubuntu 22.04+,

être compatible avec subtensor RaoFoundation,

gérer les erreurs proprement,

rester léger (pas de dépendances inutiles).

5.1 — Lancement local
bash
python3 miner.py
5.2 — Intégration subtensor
Le miner doit implémenter :

une boucle d’écoute,

une fonction de réponse,

une gestion des métadonnées,

une compatibilité avec les messages du réseau.

# 06 — Structure recommandée du code
Voici la structure recommandée pour miner.py :

Code
miner/
 ├── miner.py
 ├── MINER.md
 ├── config.json (optionnel)
 ├── utils/ (optionnel)
 └── logs/ (optionnel)
Et dans miner.py :

class CatarMiner:

__init__()

load_config()

listen()

process_question()

generate_response()

send_response()

# 07 — Contraintes conceptuelles
Le Miner doit respecter :

la logique du JEu,

la structure Absolu/Relatif,

la distinction Moije / Soije,

les invariants du Passage CATAR,

la neutralisation des dérives cognitives.

Aucune réponse ne doit :

contredire le Corpus,

introduire une stratégie de domination,

manipuler le Validator,

altérer la cohérence conceptuelle.

# 08 — Contraintes économiques
Le Miner participe à l’économie interne :

50% des émissions lui sont attribuées,

en fonction de sa participation et de sa stabilité,

sans possibilité de manipulation,

sans avantage structurel sur les validateurs.

# 09 — Tests et validation
Chaque mise à jour du Miner doit inclure :

un test minimal,

un test Ubuntu,

un test de cohérence conceptuelle,

un test de compatibilité subtensor.

Les tests doivent être reproductibles et documentés.

# 10 — Contribution au Miner
Les contributions doivent respecter :

la modularité,

la documentation,

la cohérence conceptuelle,

la stabilité cognitive,

la gouvernance par conviction.

Voir :
📄 CONTRIBUTING.md  
📄 GOVERNANCE.md  
📄 SECURITY.md
