    📩 DMALL Bot Discord

Un bot Discord simple permettant d’envoyer un message privé à tous les membres d’un serveur (commande réservée aux administrateurs).

    ⚠️ Avertissement

Attention : L’envoi massif de messages privés peut être considéré comme du spam par Discord et entraîner la suspension de ton compte ou du bot.
Utilise ce script uniquement à des fins éducatives ou sur un serveur privé/test.

    🚀 Installation

1. Installer les dépendances

Assure-toi d’avoir Python 3.8+ installé.
Puis installe les modules nécessaires :

pip install -U discord.py

    ⚙️ Configuration

Ouvre le fichier DMALL.py

Remplace la ligne suivante par le token de ton bot Discord :

TOKEN = "TON_TOKEN_ICI"


(Optionnel) Tu peux modifier le préfixe des commandes (+ par défaut) :

PREFIX = "+"

    ▶️ Lancer le bot

Exécute simplement le script,
Si tout fonctionne, tu verras dans le terminal :

✅ Connecté en tant que NOM_DU_BOT.


    💻 Utilisation
Commande principale :
+dmall <message>


Exemple :

+dmall Bonjour à tous ! 🎉


➡️ Le bot enverra ce message en DM à chaque membre du serveur (hors bots).

    🔒 Permissions

Seuls les administrateurs du serveur peuvent utiliser +dmall.

Si un utilisateur sans permission essaie, il recevra un message d’erreur.

    ❌ Gestion des erreurs

Le bot ignore les bots du serveur.

Les utilisateurs ayant bloqué les MP ne recevront pas le message (comptés comme "échecs").
