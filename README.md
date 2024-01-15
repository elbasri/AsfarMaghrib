# ASFAR MAGHRIB

## Introduction

Ce projet représente une étape essentielle dans la consolidation et l'application pratique de nos connaissances théoriques et techniques en matière de systèmes de gestion de bases de données. L'objectif principal est de concevoir et implémenter une base de données relationnelle sur Microsoft SQL Server, accompagnée d'une interface utilisateur développée en Python pour interagir avec et visualiser les résultats des requêtes.


## Fonctionnalités

-     Création de données fictives : Le projet permet de générer des données fictives pour les entités telles que les véhicules, les employés, les lignes, les tickets, etc., afin de simuler un environnement de gestion de transport.

-     Personnalisation des données fictives : Vous pouvez personnaliser les données fictives générées en modifiant les listes de noms et d'autres attributs dans le code source.

-     Création de vues de base de données : Le projet propose des vues de base de données telles que "Chauffeur" et "AgentGuichet" qui héritent des attributs de la table "Employe" et ajoutent leurs propres attributs spécifiques.

-     Audit des mises à jour d'employés : Une table "AuditEmploye" est créée pour enregistrer les modifications d'état des employés, offrant ainsi une trace des opérations effectuées.

-     Triggers SQL pour l'audit : Le projet inclut un déclencheur SQL pour enregistrer les changements d'état des employés dans la table "AuditEmploye" lorsqu'une mise à jour est effectuée.

-     Requêtes SQL avancées : Vous pouvez exécuter des requêtes SQL avancées pour extraire des informations spécifiques de la base de données, comme les ventes de tickets par employé sur une période donnée.

-     Intégration avec Django Admin : Le projet s'intègre avec l'interface d'administration de Django, vous permettant de gérer facilement les données générées et d'accéder aux fonctionnalités de l'application via "/admin/webapp".

-     Déploiement sur un domaine public : Le projet "Asfar Maghrib" est déployé sur le domaine public "asfarmaghrib.maktab.ma" et est accessible via Internet.

## Mise en route

### Prérequis

Avant de commencer à travailler sur le projet ou à le déployer, assurez-vous d'avoir les éléments suivants :

- Environnement Python : Assurez-vous d'avoir Python installé sur votre système. Vous pouvez télécharger la dernière version de Python depuis le site officiel de Python.

- Django : Le projet "Asfar Maghrib" utilise le framework Django. Vous devez donc installer Django en utilisant la commande suivante :

   ``` pip install Django   ```
   ``` pip install mssql   ```

- Base de données SQL Server : Le projet est conçu pour fonctionner avec Microsoft SQL Server. Assurez-vous d'avoir une instance de SQL Server installée et configurée sur votre système. Vous devrez également configurer les informations de connexion dans le fichier de configuration Django.

- Accès à Internet : Si vous souhaitez déployer le projet sur un domaine public et accéder à Internet, assurez-vous d'avoir une connexion Internet active et la possibilité d'héberger votre application Django en ligne.

- Base de données vide : Pour éviter tout conflit, assurez-vous d'avoir une base de données vide prête à être utilisée par le projet. Vous pouvez créer une base de données SQL Server vide via l'interface de gestion de SQL Server.

- Connaissances en SQL : Si vous prévoyez de créer des vues, des déclencheurs ou d'exécuter des requêtes SQL avancées, il est recommandé d'avoir une certaine connaissance en SQL pour comprendre et personnaliser ces fonctionnalités.

- Éditeur de code : Utilisez un éditeur de code de votre choix pour travailler sur le projet. Certains éditeurs populaires incluent Visual Studio Code, PyCharm, Sublime Text, etc.

### Installation

Pour installer et exécuter le projet localement, Clonez le dépôt du projet depuis GitHub :
   ```
   $ git clone https://github.com/votre-nom-utilisateur/votre-projet.git
```

### Demonstration
   ```
  https://asfarmaghrib.maktab.ma 
```
