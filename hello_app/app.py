# Importer les modules nécessaires de la bibliothèque Flask
from flask import Flask, render_template, request, redirect, url_for

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route("/")
def index():
    # Rendre la template 'hello.html' pour la page d'accueil
    return render_template('hello.html')

# Définir la route pour la page de bienvenue
@app.route("/hello", methods=['GET'])
def welcome():
    # Récupérer le paramètre 'nom' de la requête GET
    nom = request.args.get('nom')
    # Retourner un message de bienvenue personnalisé
    return f'Welcome, {nom}'

# Lancer l'application si le script est exécuté directement
if __name__ == "__main__":
    # Lancer l'application en mode debug
    app.run(debug=True)
