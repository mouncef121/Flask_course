# Importer les modules nécessaires de la bibliothèque Flask et sqlite3
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# Fonction pour créer l'application Flask
def create_app():
    # Créer une instance de l'application Flask
    app = Flask(__name__)

    # Définir la route pour la page d'accueil
    @app.route('/')
    def index():
        # Rendre la template 'index.html' pour la page d'accueil
        return render_template('index.html')

    # Définir la route pour la page d'inscription
    @app.route('/register')
    def register():
        # Rendre la template 'register.html' pour la page d'inscription
        return render_template('register.html')

    # Définir la route pour traiter l'inscription
    @app.route('/registrants', methods=['POST', 'GET'])
    def i_register():
        # Vérifier si la méthode de requête est POST
        if request.method == 'POST':
            # Récupérer les valeurs de l'email et du mot de passe à partir du formulaire
            email = request.form['email']
            password = request.form['password']
            # Se connecter à la base de données sqlite3
            conn = sqlite3.connect('registrant1.db')
            # Créer un curseur pour exécuter des requêtes SQL
            db = conn.cursor()
            # Exécuter une requête pour récupérer les emails existants
            db.execute("SELECT email FROM users")
            # Récupérer les emails existants
            emails = [row[0] for row in db.fetchall()]
            # Vérifier si l'email est déjà existant
            if email not in emails:
                # Exécuter une requête pour insérer les données de l'utilisateur
                db.execute('INSERT INTO users(email, password) VALUES (?,?)', (email, password))
                # Valider les modifications
                conn.commit()
                # Fermer la connexion à la base de données
                conn.close()
                # Rediriger vers la page de l'utilisateur
                return redirect(url_for('registrant', email=email))
            else:
                # Fermer la connexion à la base de données
                conn.close()
                # Rendre la template 'register.html' avec un message d'erreur
                return render_template('register.html', error='Email already exists')
        # Retourner un message d'erreur si la méthode de requête n'est pas POST
        return "error"

    # Définir la route pour afficher les informations de l'utilisateur
    @app.route('/registrantinfo/<email>')
    def registrant(email):
        # Se connecter à la base de données sqlite3
        conn = sqlite3.connect('registrant1.db')
        # Créer un curseur pour exécuter des requêtes SQL
        db = conn.cursor()
        # Exécuter une requête pour récupérer les informations de l'utilisateur
        db.execute('SELECT email FROM users WHERE email = ?', (email,))
        # Récupérer les informations de l'utilisateur
        result = db.fetchone()
        # Fermer la connexion à la base de données
        conn.close()
        # Vérifier si l'utilisateur existe
        if result:
            # Rendre la template 'registrants.html' avec les informations de l'utilisateur
            return render_template('registrants.html', email=email)
        else:
            # Retourner un message d'erreur
            return "error"

    # Définir la route pour la page de connexion
    @app.route('/login')
    def login():
        # Rendre la template 'login.html' pour la page de connexion
        return render_template('login.html')

    # Définir la route pour traiter la connexion
    @app.route('/loged', methods=['POST'])
    def loged():
        # Vérifier si la méthode de requête est POST
        if request.method == 'POST':
            # Récupérer les valeurs de l'email et du mot de passe à partir du formulaire
            email = request.form['email']
            password = request.form['password']
            # Se connecter à la base de données sqlite3
            conn = sqlite3.connect('registrant1.db')
            # Créer un curseur pour exécuter des requêtes SQL
            db = conn.cursor()
            # Exécuter une requête pour récupérer les informations de l'utilisateur
            db.execute("SELECT email, password FROM users WHERE email = ?", (email,))
            # Récupérer les informations de l'utilisateur
            user = db.fetchone()
            # Fermer la connexion à la base de données
            conn.close()
            # Vérifier si l'utilisateur existe et si le mot de passe est correct
            if user and user[1] == password:
                # Rendre la template 'loged.html' avec les informations de l'utilisateur
                return render_template('loged.html', Email=email)
            else:
                # Rendre la template 'login.html' avec un message d'erreur
                return render_template('login.html', error='Invalid email or password')
        # Rediriger vers la page de connexion si la méthode de requête n'est pas POST
        return redirect('/login')

    # Retourner l'application Flask
    return app
