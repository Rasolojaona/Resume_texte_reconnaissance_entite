# Projet : Résumé Automatique et Reconnaissance d'Entités avec Transformers

![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)
![Transformers](https://img.shields.io/badge/Transformers-4.30.2-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green)

Ce projet utilise la bibliothèque **Transformers** de Hugging Face pour générer des résumés automatiques et extraire des entités nommées (NER) à partir de textes. Il est optimisé pour fonctionner sur des systèmes avec des ressources limitées (CPU, RAM < 8 Go).

---

## Table des Matières

1. [Introduction](#introduction)
2. [Fonctionnalités](#fonctionnalités)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Endpoints](#endpoints)
6. [Exemples](#exemples)
7. [Structure du Projet](#structure-du-projet)
8. [Déploiement](#déploiement)
9. [Contributions](#contributions)
10. [Contact](#contact)

---

## Introduction

Ce projet vise à montrer comment intégrer des modèles linguistiques pré-entraînés dans une API RESTful pour :

- **Résumer des textes longs** en générant des résumés courts et cohérents.
- **Extraire des entités nommées** (personnes, organisations, lieux, etc.) à partir de textes donnés.

Les tâches sont réalisées en utilisant des pipelines de la bibliothèque **Transformers** de Hugging Face. Le projet est conçu pour être exécuté localement avec des ressources minimales, tout en offrant des performances solides.

---

## Fonctionnalités

- **Résumé Automatique** : Résume un texte donné en utilisant un modèle léger (`pipeline fonction`).
- **Reconnaissance d'Entités Nommées (NER)** : Identifie des entités spécifiques dans un texte donné.
- **Optimisé pour les Ressources Limitées** : Les modèles sont choisis pour minimiser l'utilisation de la mémoire et du CPU.
- **API FastAPI** : Expose les fonctionnalités via une API RESTful facile à utiliser.
- **Documentation Swagger** : Une interface intuitive est générée automatiquement pour tester les endpoints.

---

## Installation

### Prérequis

- Python 3.8+
- Git
- Pip
- virtualenv

### Étapes

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-nom-utilisateur/nom-du-projet.git
   cd Resume_texte_reconnaissance_entite
   ```

2. Virtualenv:

   ```terminal
   python -m venv env
   ```

3. Installation:

   ```terminal
   pip install -r requirements.txt
   ```

4. Lancement:

   ```terminal
   cd Resume_texte_reconnaissance_entite/api
   uvicorn api.app:app --reload

   cd Resume_texte_reconnaissance_entite/interface
   streamlit run app.py
   ```

5. Api:

   ```
   http://127.0.0.1:8000/docs#/

   ```

6. Interface:

   ```
   http://127.0.0.1:8502

   ```
