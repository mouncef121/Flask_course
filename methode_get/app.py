# Importer les modules nécessaires de la bibliothèque Flask
from flask import Flask, request, render_template

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route("/")
def index():
    # Rendre la template 'index.html' pour la page d'accueil
    return render_template('index.html')

# Définir la route pour la page de salutation
@app.route("/greet")
def greet():
    # Récupérer le paramètre 'name' à partir de la requête GET
    name = request.args.get('name')
    # Retourner un message de salutation personnalisé avec le nom de l'utilisateur
    return f'hello, {name}'
