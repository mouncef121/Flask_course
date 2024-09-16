# Importer les modules nécessaires de la bibliothèque Flask
from flask import Flask, url_for, redirect, request, make_response, render_template

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route('/')
def index():
    # Rendre la template 'index.html' pour la page d'accueil
    return render_template('index.html')

# Définir la route pour définir un cookie
@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    # Récupérer le nom de l'utilisateur à partir du formulaire
    name = request.form.get('name')
    # Créer une réponse avec un message de confirmation
    resp = make_response("Cookie a été défini!")
    # Définir le cookie 'nom_utilisateur' avec la valeur du nom de l'utilisateur
    resp.set_cookie('nom_utilisateur', name)
    # Retourner la réponse avec le cookie défini
    return resp

# Définir la route pour récupérer la valeur d'un cookie
@app.route('/get_cookie')
def get_cookie():
    # Récupérer la valeur du cookie 'nom_utilisateur'
    nom_utilisateur = request.cookies.get('nom_utilisateur')
    # Vérifier si le cookie existe
    if nom_utilisateur:
        # Retourner un message avec le nom de l'utilisateur si le cookie existe
        return f'Le nom de l\'utilisateur est {nom_utilisateur}'
    else:
        # Retourner un message si le cookie n'existe pas
        return "Aucun cookie trouvé!"

# Définir la route pour supprimer un cookie
@app.route('/delete_cookie')
def delete_cookie():
    # Créer une réponse avec un message de confirmation
    resp = make_response("Le cookie a été supprimé!")
    # Supprimer le cookie 'nom_utilisateur'
    resp.delete_cookie('nom_utilisateur')
    # Retourner la réponse avec le cookie supprimé
    return resp

# Lancer l'application si le script est exécuté directement
if __name__ == '__main__':
    # Lancer l'application en mode debug
    app.run(debug=True)
