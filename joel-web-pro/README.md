# Joël Web Pro Solution — Site vitrine (Flask)

Site vitrine professionnel pour **Joël Web Pro Solution**, avec bouton flottant
WhatsApp et bouton "Commander / Prendre rendez-vous" sur chaque service,
qui ouvre directement une conversation WhatsApp pré-remplie vers le
**+237 659 026 444**.

## Installation

```bash
cd joel-web-pro
python3 -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install -r requirements.txt
```

## Lancer le site en local

```bash
python app.py
```

Puis ouvrez **http://127.0.0.1:5000** dans votre navigateur.

## Structure du projet

```
joel-web-pro/
├── app.py                  # Application Flask (routes + contenu des services)
├── requirements.txt
├── templates/
│   └── index.html          # Page unique (hero, services, contact, widget WhatsApp)
└── static/
    ├── css/style.css       # Design (charte bleu nuit / cyan reprise de l'affiche)
    └── js/script.js        # Ouverture/fermeture du widget WhatsApp
```

## Personnaliser

- **Numéro WhatsApp / e-mail** : modifiez `WHATSAPP_NUMBER`, `CONTACT_EMAIL`
  et `CONTACT_PHONE_DISPLAY` en haut de `app.py`.
- **Services** : ajoutez, modifiez ou supprimez une entrée dans la liste
  `SERVICES` de `app.py` — le site se met à jour automatiquement (icône,
  titre, description, message WhatsApp pré-rempli).
- **Message d'accroche** : les 4 questions de la section "Ça vous parle ?"
  sont dans la liste `PAIN_POINTS` de `app.py`.
- **Couleurs** : variables `:root` en haut de `static/css/style.css`.

## Mise en ligne (déploiement)

Le projet est un site Flask classique, déployable sur n'importe quel
hébergeur Python (Render, Railway, PythonAnywhere, un VPS avec Gunicorn +
Nginx, etc.). Pour la production, lancez-le avec un serveur WSGI, par
exemple :

```bash
pip install gunicorn
gunicorn app:app
```

### Déploiement sur Vercel

Le projet contient déjà tout ce qu'il faut pour Vercel :
- `api/index.py` — point d'entrée serverless qui réexpose l'app Flask
- `vercel.json` — configuration (routes + fichiers à inclure)

**Option A — via le site Vercel (le plus simple)**
1. Mettez le dossier `joel-web-pro` dans un dépôt GitHub (créez le repo,
   `git init`, `git add .`, `git commit -m "init"`, `git push`).
2. Sur [vercel.com](https://vercel.com), cliquez sur **Add New → Project**
   et importez ce dépôt.
3. Vercel détecte automatiquement `vercel.json` — laissez les réglages par
   défaut et cliquez sur **Deploy**.
4. Votre site est en ligne sur une adresse `https://....vercel.app`.

**Option B — via la CLI Vercel**
```bash
npm install -g vercel
cd joel-web-pro
vercel        # suit les questions, déploiement de test
vercel --prod # déploiement en production
```

**À savoir**
- Vercel exécute Flask comme une fonction serverless : pas de serveur qui
  tourne en continu, chaque requête démarre une fonction (léger délai au
  premier appel après une période d'inactivité, normal et sans impact sur
  le fonctionnement du site).
- Pour un nom de domaine personnalisé, ajoutez-le dans l'onglet
  **Settings → Domains** du projet sur Vercel.
