# Importer les modules nécessaires de la bibliothèque Flask et Flask-Session
from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import time

# Créer une instance de l'application Flask
app = Flask(__name__)

# Configuration de l'application
# Définir la session comme non permanente
app.config["SESSION_PERMANENT"] = False
# Définir le type de session comme fichier système
app.config["SESSION_TYPE"] = "filesystem"

# Initialiser la session avec l'application
Session(app)

# Définir la route pour la page d'accueil
@app.route('/')
def index():
    # Rendre la template 'index.html' pour la page d'accueil
    # avec la langue sélectionnée en session
    return render_template('index.html', lang = session.get('lang'))

# Définir la route pour définir la langue
@app.route('/lang', methods = ["POST"])
def lang():
    # Récupérer la langue sélectionnée à partir du formulaire
    session['lang'] = request.form.get('lang')
    
    # Retourner un message de confirmation avec la langue sélectionnée
    return f'votre language is : {session["lang"]}'
