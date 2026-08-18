📄 INSTALLATION.md
Guide d’accès, d’installation et de navigation dans le Subnet CATAR
Version 2.0 — Mise à jour conceptuelle + applicative

# 01 — Prérequis
Le Subnet CATAR peut être utilisé de deux manières :

1.1 — Mode conceptuel (sans installation)
Le Subnet CATAR est un système conceptuel qui peut être utilisé :

en lisant les fichiers du dépôt,

en répondant aux questionnaires,

en suivant la logique du Passage CATAR,

en complétant les modules 01 → 05.

Aucun programme, aucune dépendance, aucun environnement technique n’est requis pour ce mode.
C’est le mode décrit dans ton fichier actuel .

1.2 — Mode applicatif (avec installation)
Pour utiliser le Subnet CATAR comme subnet Bittensor (miner + validator), il faut :

un système Ubuntu 22.04+,

Python 3.10+,

Git,

Cargo / Rust,

l’installation de Subtensor (RaoFoundation),

le dépôt CATAR cloné localement.

Ce mode permet d’exécuter :

le Miner CATAR minimal viable,

le Validator CATAR conceptuel,

les scripts de gestion de conviction,

les tests de fonctionnement.

# 02 — Structure du dépôt
Le dépôt est organisé en modules conceptuels et techniques :

Module	Fonction
01 — Questionnaire‑Test	État cognitif initial
02 — Corpus CATAR	Transformation conceptuelle
03 — Contrôle de Connaissance	Vérification de l’intégration
04 — Correction	Réponses officielles
05 — Compte‑Rendu	Résultats, analyse, historique
miner/	Miner CATAR minimal viable
validator/	Validator conceptuel
governance/	Scripts de conviction
docs/	Documentation multilingue


Chaque module contient :

un README explicatif,

les fichiers nécessaires à son étape .

# 03 — Installation du Subnet CATAR (mode applicatif)
3.1 — Installer Subtensor (RaoFoundation)
bash
git clone https://github.com/RaoFoundation/subtensor.git
cd subtensor
cargo build --release
3.2 — Cloner le Subnet CATAR
bash
git clone https://github.com/QuatreCATAR/catar-subnet.git
cd catar-subnet
3.3 — Installer les dépendances Python
bash
pip install -r requirements.txt
3.4 — Lancer le Miner CATAR
bash
python3 miner/miner.py
3.5 — Lancer le Validator CATAR
bash
python3 validator/validator.py
3.6 — Activer les émissions (optionnel)
bash
subtensor subnet set-emission --netuid <ID>
3.7 — Gérer la conviction (optionnel)
bash
subtensor stake lock --amount <TAO>
# 04 — Mode conceptuel (sans installation)
Pour utiliser le Subnet CATAR sans aucune installation, suivez simplement les modules dans l’ordre :

01 — Questionnaire‑Test

02 — Corpus CATAR

03 — Contrôle de Connaissance

04 — Correction

05 — Compte‑Rendu + Analyse + Historique

Cet ordre correspond exactement à ton fichier actuel .

Le guide complet du Passage se trouve dans :
📄 GUIDE-DU-PASSAGE.md

# 05 — Navigation recommandée
Ordre officiel des modules :

Code
01 → 02 → 03 → 04 → 05 → retour à 01
Détail :

Test initial

Lecture du Corpus

Contrôle de Connaissance

Correction

Compte‑Rendu + Analyse + Historique

Rebouclage vers un nouveau Passage

# 06 — Utilisation hors‑ligne
Le Subnet CATAR peut être utilisé :

en ligne (GitHub),

hors‑ligne (ZIP),

dans un environnement IA,

dans un environnement humain.

Pour une utilisation hors‑ligne :

Cliquer sur Code → Download ZIP

Extraire le dossier

Naviguer dans les modules comme sur GitHub

# 07 — Mise à jour du Subnet
Les mises à jour sont indiquées dans :

📄 VERSION.md

Pour mettre à jour votre copie :

re‑télécharger le ZIP,

ou utiliser git pull.

# 08 — Documentation complémentaire
Les fichiers recommandés :

GUIDE-DU-PASSAGE.md

Cycle-CATAR.md

VERSION.md

README.md (multilingue)

ROADMAP.md

CONTRIBUTING.md

# 09 — Support et contributions
Pour toute question ou suggestion :

ouvrir une Issue GitHub,

ou proposer une Pull Request.

Le Subnet CATAR est conçu pour évoluer.
