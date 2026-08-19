# README‑TECHNIQUE.md  
Documentation technique — HuggingFace‑CATAR  
Version 1.1 — Architecture, modules et exécution

---

## 01 — Objectif

Ce document fournit une description technique détaillée du projet **HuggingFace‑CATAR**.  
Il est destiné aux développeurs et contributeurs afin de :  
- comprendre l’architecture interne,  
- maîtriser les modules conceptuels et techniques,  
- exécuter correctement le miner et le validator,  
- respecter les invariants conceptuels du Corpus CATAR.

---

## 02 — Architecture générale

Le projet est structuré en deux ensembles complémentaires :

### Modules techniques
- `miners/` : génération et transformation de données conceptuelles  
- `validators/` : évaluation et stabilisation des transmissions  
- `scripts/` : automatisation, supervision et lancement parallèle  
- `config/` : paramètres et configuration (`settings.yaml`)  
- `tests/` : tests unitaires et conceptuels  
- `catar_core/` : noyau technique et logique interne  

### Modules conceptuels
- **01 — Questionnaire‑Test**  
- **02 — Corpus CATAR**  
- **03 — Contrôle de Connaissance**  
- **04 — Correction**  
- **05 — Compte‑Rendu / Analyse hermétique**

---

## 03 — Miner CATAR

Le miner est minimal viable :  
- génère des données conceptuelles,  
- respecte la logique du Passage CATAR,  
- reste neutre et sans biais conceptuel,  
- interagit avec subtensor (optionnel).  

Exécution locale :  
```bash
python3 miners/miner.py
```
## 04 — Validator CATAR
Le validator est conceptuel et neutre :

évalue la cohérence des transmissions,

respecte les invariants du Corpus,

utilise explicitement settings.yaml pour la configuration.

Exécution locale :
python3 validators/validator.py

## 05 — Scripts
Les scripts permettent :

lancement parallèle des modules,

gestion des logs,

supervision,

redémarrage automatique en cas d’erreur.

## 06 — Configuration
Le fichier config/settings.yaml contient :

chemins des modules,

paramètres d’exécution,

configuration subtensor (optionnelle).

Le validator utilise explicitement ce fichier pour garantir la reproductibilité.

## 07 — Tests
Les tests sont organisés dans tests/ :

tests conceptuels (logique du Passage),

tests de cohérence,

tests de stabilité cognitive,

tests unitaires techniques.

Exécution :

bash
pytest tests/

## 08 — Intégration subtensor (optionnelle)
Le projet peut être relié à subtensor pour :

activation des émissions,

locking volontaire,

challenge,

maturation.

Commandes utiles :

bash
btcli wallet new
btcli stake add
btcli run miner
btcli run validator

## 09 — Économie interne
Le modèle économique est basé sur la symétrie :

50% validateurs

50% miners

⚠️ Dans HuggingFace‑CATAR, ce modèle est neutralisé : il sert uniquement de référence conceptuelle.

## 10 — Roadmap technique
Phases principales :

stabilisation du subnet,

gouvernance par conviction,

Passage automatisé,

Novelty Search.

Voir ROADMAP.md pour le détail complet.

## 11 — Bonnes pratiques
respecter les invariants conceptuels,

ne jamais modifier le Corpus CATAR,

documenter chaque ajout,

écrire des tests reproductibles,

garder le code simple et lisible,

assurer la transmissibilité du projet.


