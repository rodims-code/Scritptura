```markdown
# Scriptura 📖✨

> Une plateforme numérique moderne, minimaliste et haut de gamme dédiée à l'étude et à l'évaluation des livrets de cours bibliques.

**Scriptura** transpose l'expérience des livrets de formation papier (comme le cursus des Centres Bibliques) en une application web interactive ultra-rapide. Elle permet aux étudiants de remplir leurs leçons de manière dynamique (QCM, mots croisés, textes à trous) et offre aux correcteurs un espace dédié pour évaluer les progrès et attribuer les notes.

---

## 🚀 Fonctionnalités Clés

### 👤 Gestion des Utilisateurs & Authentification
- **Inscription simplifiée :** L'étudiant s'inscrit avec son Nom, Prénom, Email, Téléphone, Adresse et Pays. Le système génère automatiquement un `username` technique unique en arrière-plan (ex: `dieuveil-rodims`).
- **Connexion double méthode :** Authentification sécurisée via **Email** ou via le **Code Élève** unique (ex: `01.0052`) hérité du système papier historique.
- **Rôles applicatifs :** Séparation stricte des accès entre **Étudiants**, **Enseignants/Correcteurs** et **Administrateurs**.

### 📚 Gestion du Cursus Pédagogique
- **Structure en cascade :** Parcours complet (`Cursus`) ➔ Livrets thématiques (`Livret` ex: *C2 - Évangile selon Marc*) ➔ Chapitres (`Leçon`) ➔ Exercices (`Question`).
- **Exercices dynamiques & interactifs :** Prise en charge de multiples formats grâce à un moteur de configuration flexible basé sur le format `JSON` :
  - **QCM** (Choix multiples)
  - **Textes à trous**
  - **Questions ouvertes** (avec correction humaine)
  - **Éléments à relier** (système de paires)
  - **Le Verset Caché / Mots croisés** (grilles interactives générées dynamiquement en SvelteKit)

### 📊 Suivi & Évaluation (Le Relevé Numérique)
- **Tableau de progression :** Version numérique du carton d'évaluation physique pour suivre en temps réel le statut d'une leçon (`Verrouillé`, `En cours`, `Soumis`, `Corrigé`).
- **Système de notation :** Sauvegarde des réponses exactes de l'élève, calcul automatique des points pour les exercices standard, et interface de relecture avec feedbacks textuels pour les enseignants.

---

## 🛠️ Stack Technique

L'architecture est pensée pour l'interopérabilité (API-first) et la rapidité d'exécution.

| Composant | Technologie | Rôle |
| :--- | :--- | :--- |
| **Frontend** | **SvelteKit** | Framework d'interface réactif, performant et optimisé. |
| **Styles & UI** | **Tailwind CSS + DaisyUI** | Design système minimaliste, épuré et *premium*. |
| **Icons** | **Lucide Svelte** | Pack d'icônes vectorielles modernes et légères. |
| **Backend** | **Django + DRF** | API robuste, gestion de la logique métier et sécurité de la DB. |
| **Auth Token** | **Simple JWT** | Authentification stateless sécurisée par jetons d'accès. |
| **Base de Données** | **PostgreSQL** (ou SQLite en dev) | Stockage relationnel et manipulation de configurations complexes en `JSONField`. |

---

## 📐 Architecture de la Base de Données (Modèle Conceptuel)

Le schéma relationnel est conçu en **DBML** (Database Markup Language) et gère les dépendances structurelles suivantes :


```

[CURSUS] 1 ── * [LIVRET] 1 ── * [LECON] 1 ── * [QUESTION]
│               │
▼               ▼
[USER] 1 ────────────────── * [PROGRESSION]   [USER_ANSWER]

```
*Le diagramme complet, visuel et interactif est modélisable directement sur [dbdiagram.io](https://dbdiagram.io).*

---

## ⚙️ Installation et Démarrage (Développement)

### 1. Prérequis
- Python 3.10+
- Node.js 18+

### 2. Clonage du projet
```bash
git clone [https://github.com/RODIMS-CODE/Scriptura.git](https://github.com/RODIMS-CODE/Scriptura.git)
cd Scriptura

```

### 3. Configuration du Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

```

*L'API sera disponible sur `http://127.0.0.1:8000/`.*

### 4. Configuration du Frontend (SvelteKit)

```bash
cd ../frontend
npm install
npm run dev -- --open

```

*L'interface web s'ouvrira sur `http://localhost:5173/`.*

---

## ✒️ Auteur

Développé avec passion par **RODIMS-CODE** (Dieuveil Emmanuel Rodim's Miekountima).
N'hésitez pas à ouvrir une *Issue* ou une *Pull Request* pour contribuer au projet !
