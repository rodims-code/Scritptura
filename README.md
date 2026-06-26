# Scriptura 📖✨

> Une plateforme web moderne, minimaliste et haut de gamme pour l'étude et l'évaluation des livrets de cours bibliques.

Scriptura transpose l'expérience des livrets papier (comme le cursus des Centres Bibliques) en une application web interactive, rapide et accessible depuis n'importe quel navigateur.

---

## 🚀 En un coup d'œil

- Public ciblé : étudiants, enseignants/correcteurs et administrateurs pédagogiques.
- Objectif : numériser les livrets de cours, faciliter la passation des exercices et centraliser le suivi pédagogique.
- Points forts : interface réactive (SvelteKit), API RESTful (Django + DRF), configuration d'exercices flexible (JSON).

---

## ✨ Fonctionnalités principales

### 👥 Gestion des utilisateurs & authentification
- Inscription simplifiée (Nom, Prénom, Email, Téléphone, Adresse, Pays) ; génération automatique d'un username technique.
- Connexion par Email ou par Code Élève (ex. `01.0052`).
- Rôles : Étudiant, Enseignant/Correcteur, Administrateur (contrôle fin des accès).

### 📚 Organisation du cursus
- Structure hiérarchique : Cursus → Livrets → Leçons → Questions.
- Types d'exercices pris en charge via un moteur de configuration JSON :
  - QCM
  - Textes à trous
  - Questions ouvertes (correction humaine)
  - Éléments à relier (paires)
  - Grilles interactives (Verset caché / Mots croisés)

### 📊 Suivi & évaluation
- Tableau de progression : statuts de leçon (`Verrouillé`, `En cours`, `Soumis`, `Corrigé`).
- Calcul automatique des points pour les exercices standard et interface de relecture pour les exercices corrigés manuellement.
- Historique des réponses et relevés numériques individuels.

---

## 🛠️ Stack technique

L'architecture est API-first pour faciliter l'interopérabilité et l'évolution.

| Composant | Technologie | Rôle |
| :--- | :--- | :--- |
| Frontend | SvelteKit | Interface réactive et performante |
| Styles & UI | Tailwind CSS + DaisyUI | Design minimaliste et modulable |
| Icônes | Lucide Svelte | Pack d'icônes léger |
| Backend | Django + Django REST Framework | API, logique métier et sécurité |
| Auth | Simple JWT | Authentification par jetons (stateless) |
| Base de données | PostgreSQL (SQLite en dev) | Stockage relationnel avec JSONField pour config |

---

## 📐 Modèle conceptuel (aperçu)

Le modèle relationnel suit cette structure principale :

```
[CURSUS] 1 ── * [LIVRET] 1 ── * [LECON] 1 ── * [QUESTION]
│               │
▼               ▼
[USER] 1 ────────────────── * [PROGRESSION]   [USER_ANSWER]
```

Le diagramme complet est modélisable sur https://dbdiagram.io.

---

## ⚙️ Installation & démarrage (développement)

Prérequis : Python 3.10+, Node.js 18+

1. Cloner le projet

```bash
git clone https://github.com/rodims-code/Scritptura.git
cd Scritptura
```

2. Backend (Django)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

L'API sera disponible sur http://127.0.0.1:8000/.

3. Frontend (SvelteKit)

```bash
cd ../frontend
npm install
npm run dev -- --open
```

L'interface se lancera typiquement sur http://localhost:5173/.

---

## 🧭 Contribution

Les contributions sont bienvenues :
- Ouvrez une Issue pour signaler un bug ou proposer une amélioration.
- Soumettez une Pull Request avec une description claire des changements.

Quelques idées : ajouter des types d'exercices, améliorer l'UX mobile, internationalisation.

---

## 📝 Licence

Précisez ici la licence (ex : MIT) si vous souhaitez en ajouter une.

---

## ✒️ Auteur

Développé avec passion par **RODIMS-CODE** (Dieuveil Emmanuel Rodim's Miekountima).

Contact / contributions : ouvrez une Issue ou une Pull Request sur ce dépôt.
