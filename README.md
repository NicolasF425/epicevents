## Application Python dans le cadre d'une formation

Notes : ce projet a été développé sous Windows. 

Des ajustements sur le code et la procédure peuvent être nécessaires pour une utilisation sous Linux.

Pour des question de limitation de temps de développement, des controles sur les valeurs entrées ne sont pas effectués.

### Description du contexte du projet

 Epic Events est une entreprise qui organise des événements (fêtes,
 réunions professionnelles, manifestations hors les murs) pour ses clients.
 Nous souhaitons développer un logiciel CRM (Customer Relationship
 Management) pour améliorer notre travail.
 Le logiciel CRM permet de collecter et de traiter les données des clients
 et de leurs événements, tout en facilitant la communication entre les
 différents pôles de l'entreprise.

### **Prérequis :** 

+ Un environnement de développement (VSCode, Pycharm...)
+ Python 3.X
+ avoir installé pip (gestionnaire de packages pour python) s'il n'est pas présent
+ avoir installé MySQL et créé une base "epicevents"

### exécution des commandes

Sous Windows : avec la ligne de commandes (cmd)

Sous Linux : dans le bash

### Pour récuperer les fichiers du projet :

exécuter : git clone https://github.com/NicolasF425/epicevents.git

**Activation sur Windows :**

exécuter à partir du répertoire projet: env\Scripts\activate

**Activation sur MacOS/Linux :**

exécuter à partir du répertoire projet: source env/bin/activate

### **Pour installer les dépendances :**

Aller dans le répertoire du projet puis exécuter : pip install -r requirements.txt

Le fichier requirements.txt doit être présent dans le dossier du projet

### Paramétrage du projet :

Un fichier .env doit être créé à la racine du projet ;

dsn=votre_cle_secrete_pour_sentry

sql_epicevents='votre_mot_de_passe_pour_la_base'

SECRET_KEY=votre_cle_secrete_pour_le_token

FILENAME=token.txt


