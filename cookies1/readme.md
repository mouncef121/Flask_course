**Cookie Manager**

Une application Flask simple pour gérer les cookies.

**Fonctionnalités**

* Définir un cookie avec un nom d'utilisateur
* Récupérer la valeur d'un cookie
* Supprimer un cookie

**Routes**

* `/` : Page d'accueil
* `/set_cookie` : Définir un cookie (méthode POST)
* `/get_cookie` : Récupérer la valeur d'un cookie
* `/delete_cookie` : Supprimer un cookie

**Utilisation**

1. Lancer l'application en exécutant le script `app.py`
2. Accéder à la page d'accueil à l'adresse `http://localhost:5000/`
3. Définir un cookie en envoyant une requête POST à l'adresse `http://localhost:5000/set_cookie` avec un formulaire contenant le nom de l'utilisateur
4. Récupérer la valeur du cookie en accédant à l'adresse `http://localhost:5000/get_cookie`
5. Supprimer le cookie en accédant à l'adresse `http://localhost:5000/delete_cookie`

**Dépendances**

* Flask

**Licence**

Cette application est sous licence MIT.

**Auteur**

Mouncef