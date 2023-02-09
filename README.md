# Projet-ecommerce
Contient toutes les informations nécessaires afin de récréer ce site statique avec les informations et le code
ce projet contient 2 fichiers principaux : ecommerce et instance 

- instance contient la base données 

-ecommerce contient les dossiers templates , static et les fichiers de l'architecture M.V.C 
a savoir :

-le fichier views.py (pour les routes et certaines routes de traitement + insertion)
- le fichier models.py (pour la base de données , sa création et celles de tables
-Et les autres fichiers de control
 tels que config.py  (pour la création de l'app , et quelques autres configurations ) ,
-  __init__.py pour faire les imports nécessaires afin de faire le pont entre tous les autres fichiers et le main 

dans le fichier template on a les fichiers html et un dossier auth
templates contient accueil.html et le fichier auth contient :

-session.html (correspond a la page sur laquelle celui qui se connecte arrivera)

-inscription.html (la page d'inscription)

-connexion.html (la page de connexion )

-le dossier static contient le dossier css comprenant les fichiers
 css nécessaires pour les pages du dossiers auth

mais aussi le dossier JS pour les fichiers JS des pages du dossier auth 

à la racine du fichier on peut retrouver le main.py qui est l'instance phare de démarrage du projet 
