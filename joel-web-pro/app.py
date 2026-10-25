from flask import Flask, render_template

app = Flask(__name__)

WHATSAPP_NUMBER = "237659026444"  # Cameroun +237
CONTACT_EMAIL = "joeltene100@gmail.com"
CONTACT_PHONE_DISPLAY = "+237 659 026 444"

SERVICES = [
    {
        "icon": "fa-cart-shopping",
        "title": "Création de sites e-commerce",
        "text": "Une boutique en ligne complète, pensée pour vendre : catalogue, panier, paiement et gestion des commandes.",
        "wa_msg": "Bonjour Joël, je souhaite créer un site e-commerce pour ma boutique.",
    },
    {
        "icon": "fa-calendar-check",
        "title": "Sites de prise de rendez-vous",
        "text": "Un agenda en ligne qui reçoit vos clients 24h/24, sans appels ni doubles réservations.",
        "wa_msg": "Bonjour Joël, je souhaite un site de prise de rendez-vous.",
    },
    {
        "icon": "fa-graduation-cap",
        "title": "Sites de formation en ligne",
        "text": "Une plateforme pour vendre vos cours, suivre vos apprenants et diffuser vos contenus.",
        "wa_msg": "Bonjour Joël, je souhaite créer un site de formation en ligne.",
    },
    {
        "icon": "fa-address-card",
        "title": "Sites portfolio",
        "text": "Une vitrine soignée pour présenter votre travail et convaincre en un coup d'œil.",
        "wa_msg": "Bonjour Joël, je souhaite un site portfolio.",
    },
    {
        "icon": "fa-hashtag",
        "title": "Pages professionnelles",
        "text": "TikTok, Facebook, Instagram : des pages bien construites qui donnent confiance à vos visiteurs.",
        "wa_msg": "Bonjour Joël, je souhaite créer mes pages professionnelles (TikTok/Facebook/Instagram).",
    },
    {
        "icon": "fa-rocket",
        "title": "Boostage de comptes",
        "text": "Plus de portée, plus d'abonnés, plus d'engagement sur vos réseaux sociaux.",
        "wa_msg": "Bonjour Joël, je souhaite booster mes comptes réseaux sociaux.",
    },
    {
        "icon": "fa-screwdriver-wrench",
        "title": "Dépannage logiciels & systèmes",
        "text": "Un problème informatique qui bloque votre activité ? On le règle rapidement.",
        "wa_msg": "Bonjour Joël, j'ai besoin d'un dépannage logiciel/système.",
    },
    {
        "icon": "fa-chart-line",
        "title": "Gestion de business en ligne",
        "text": "On s'occupe de votre présence en ligne pendant que vous gérez votre business.",
        "wa_msg": "Bonjour Joël, je souhaite un accompagnement pour la gestion de mon business en ligne.",
    },
    {
        "icon": "fa-comments",
        "title": "Community management",
        "text": "Des publications régulières et une communauté bien animée, sans y passer vos journées.",
        "wa_msg": "Bonjour Joël, je souhaite un service de community management.",
    },
]

PAIN_POINTS = [
    "Tu veux mettre ta boutique en ligne et tu ne sais pas par où commencer ?",
    "Tu gères tes clients à la main et ça te fait perdre du temps ?",
    "Tu n'arrives pas à booster tes comptes malgré tes efforts ?",
    "Tu galères à gérer ta clientèle en ligne ?",
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        services=SERVICES,
        pain_points=PAIN_POINTS,
        wa_number=WHATSAPP_NUMBER,
        email=CONTACT_EMAIL,
        phone_display=CONTACT_PHONE_DISPLAY,
    )


if __name__ == "__main__":
    app.run(debug=True)
