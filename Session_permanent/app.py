# Importer les modules nécessaires de la bibliothèque Flask et Flask-Session
from flask import Flask, session, render_template, redirect, url_for, request
from flask_session import Session

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la clé secrète pour l'application
app.secret_key = 'mykey1'

# Définir la route pour la page d'accueil
@app.route('/')
def index():
    # Rendre la template 'index.html' pour la page d'accueil
    return render_template('index.html')

# Définir la route pour définir les variables de session
@app.route('/set_session', methods=['POST'])
def set_session():
    # Récupérer les valeurs du nom et de l'email à partir du formulaire
    name = request.form.get('name')
    email = request.form.get('email')
    
    # Définir les variables de session pour le nom et l'email
    session['name'] = name
    session['email'] = email
    
    # Retourner un message de confirmation avec les valeurs du nom et de l'email
    return f'username : {name} and email is : {email}' #redirect('/get_session')

# Définir la route pour récupérer les variables de session
@app.route('/get_session')
def get_session():
    # Récupérer les valeurs des variables de session pour le nom et l'email
    name = session.get('name')
    email = session.get('email')
    
    # Retourner un message avec les valeurs du nom et de l'email
    return f'username : {name} and email is : {email}'

# Lancer l'application si le script est exécuté directement
if __name__ == '__main__':
    # Lancer l'application en mode debug
    app.run(debug=True)
