Une application Flask simple pour gérer les cookies.

**Fonctionnalités**

* Définir des cookies avec un nom et un email
* Récupérer les valeurs des cookies
* Supprimer les cookies

**Routes**

* `/` : Page d'accueil
* `/set_cookie` : Définir des cookies (méthode POST)
* `/get_cookie` : Récupérer les valeurs des cookies
* `/delete_cookie` : Supprimer les cookies

**Utilisation**

1. Lancer l'application en exécutant le script `app.py`
2. Accéder à la page d'accueil à l'adresse `http://localhost:5000/`
3. Définir des cookies en envoyant une requête POST à l'adresse `http://localhost:5000/set_cookie` avec un formulaire contenant le nom et l'email
4. Récupérer les valeurs des cookies en accédant à l'adresse `http://localhost:5000/get_cookie`
5. Supprimer les cookies en accédant à l'adresse `http://localhost:5000/delete_cookie`

**Dépendances**

* Flask

