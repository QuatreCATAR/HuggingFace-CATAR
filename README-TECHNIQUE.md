# 📄 README‑TECHNIQUE.md  
Guide technique pour développeurs — Subnet CATAR  
Version 1.1 — Architecture, modules, exécution, intégration subtensor

---

## 01 — Introduction technique

Le Subnet CATAR est un subnet Bittensor conçu pour :  

- produire des réponses conceptuelles (**miner**)  
- évaluer la cohérence logique et cognitive (**validator**)  
- stabiliser la cognition via le Passage CATAR (modules 01 → 05)  
- fonctionner avec une économie interne 50/50 (miners/validators)  
- être gouverné par conviction (locking volontaire)  

Ce document fournit toutes les informations nécessaires aux développeurs pour comprendre, modifier, étendre ou intégrer le Subnet CATAR.

---

## 02 — Architecture technique du dépôt

Structure réelle du dépôt :  

01-QUESTIONNAIRE-TEST/
02-CORPUS-CATAR/
03-CONTROLE-CONNAISSANCE/
04-CORRECTION/
05-COMPTE-RENDU/
catar_core/
config/
miners/
validator/
scripts/
tests/
docs/
requirements.txt
README.md
ROADMAP.md
INSTALLATION.md
GOVERNANCE.md
ECONOMY.md
SECURITY.md
VERSION.md

Code

### Modules techniques
- `miners/` — Miner CATAR minimal viable  
- `validator/` — Validator conceptuel  
- `scripts/` — Lancement parallèle miner + validator  
- `config/` — `settings.yaml` (chemins, paramètres)  
- `tests/` — tests unitaires et conceptuels  
- `catar_core/` — logique interne CATAR (compte‑rendu, analyse)  

### Modules conceptuels
- `01 → 05` : Passage CATAR complet (Test → Corpus → Contrôle → Correction → Compte‑Rendu)  

---

## 03 — Installation technique

### 3.1 — Installer Subtensor (RaoFoundation)

```bash
git clone https://github.com/RaoFoundation/subtensor.git
cd subtensor
cargo build --release
```

3.2 — Cloner le Subnet CATAR
bash
git clone https://github.com/QuatreCATAR/catar-subnet.git
cd catar-subnet
3.3 — Installer les dépendances Python
bash
pip install -r requirements.txt
04 — Miner CATAR (/miners)
4.1 — Lancement
bash
python3 miners/miner.py
4.2 — Rôle technique
écoute subtensor

reçoit une question

génère une réponse conceptuelle

transmet au validator

respecte les invariants conceptuels du Corpus

4.3 — Contraintes
pas de dérives cognitives

pas de stratégie de domination

pas de modification du Passage

neutralité conceptuelle

05 — Validator CATAR (/validator)
5.1 — Lancement
bash
python3 validator/validator.py
5.2 — Rôle technique
écoute subtensor

reçoit la réponse du miner

compare au Corpus CATAR

détecte les dérives conceptuelles

attribue un score cognitif

renvoie l’évaluation au réseau

5.3 — Contraintes
neutralité totale

reproductibilité

respect strict du Corpus

aucune influence sur le miner

06 — Scripts (/scripts)
Exemple de lancement parallèle :

bash
python3 scripts/run_parallel.py
Fonctions typiques :

gestion des processus

logs

redémarrage automatique

supervision minimale

07 — Configuration (/config)
Le fichier settings.yaml contient :

chemins des modules

paramètres du miner

paramètres du validator

options de logging

configuration subtensor

Le validator utilise explicitement ce fichier.

08 — Tests (/tests)
Tests inclus :

tests de compréhension

tests conceptuels

tests de cohérence

tests de stabilité cognitive

À ajouter par les développeurs :

tests unitaires pour miner

tests unitaires pour validator

tests d’intégration subtensor

tests de Passage CATAR automatisé (phase 3 de la roadmap)

09 — Intégration subtensor
Le Subnet CATAR est compatible avec subtensor (RaoFoundation) :

activation des émissions

locking volontaire

challenge 10%

maturation ~30 jours

Commandes utiles :

bash
subtensor subnet set-emission --netuid <ID>
subtensor stake lock --amount <TAO>
10 — Économie interne (50/50)
Le Subnet CATAR utilise un modèle économique équitable :

50% validateurs

50% miners

Implications techniques :

pas de biais dans le code

pas de mécanisme favorisant un rôle

neutralité des scripts

transparence des évaluations

11 — Gouvernance technique
La gouvernance repose sur :

conviction (locking volontaire)

maturation (~30 jours)

seuil de challenge (10%)

protection contre les prises de contrôle externes

Les développeurs doivent :

respecter la modularité

documenter chaque modification

éviter les dérives économiques

maintenir la transmissibilité du projet

12 — Roadmap technique
Phase 1 — Stabilisation
miner minimal viable

validator conceptuel

documentation multilingue

économie 50/50

Phase 2 — Gouvernance
activation des émissions

gestion du locking

sécurisation de la propriété

Phase 3 — Passage CATAR automatisé
intégration complète du Corpus

analyse automatique

historique des Passages

Phase 4 — Novelty Search
démonstration conceptuelle

publication officielle

13 — Bonnes pratiques pour développeurs
respecter les invariants conceptuels

ne jamais modifier le Passage CATAR

documenter chaque module

ajouter des tests systématiquement

maintenir la neutralité du miner et du validator

éviter les dépendances inutiles

garder le code lisible et transmissible

respecter la gouvernance par conviction
