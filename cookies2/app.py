# Importer les modules nécessaires de la bibliothèque Flask
from flask import Flask, redirect, request, make_response, render_template, url_for

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir la route pour la page d'accueil
@app.route('/')
def index():
    # Rendre la template 'index.html' pour la page d'accueil
    return render_template('index.html')

# Définir la route pour définir des cookies
@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    # Récupérer les valeurs du nom et de l'email à partir du formulaire
    name = request.form['name']
    email = request.form['email']
    
    # Créer une réponse et définir les cookies
    resp = make_response(redirect('/get_cookie'))
    resp.set_cookie('nom_utilisateur', name)
    resp.set_cookie('email', email)
    
    # Retourner la réponse avec les cookies définis
    return resp

# Définir la route pour récupérer les valeurs des cookies
@app.route('/get_cookie')
def get_cookie():
    # Récupérer les valeurs des cookies avec les noms corrects
    name = request.cookies.get('nom_utilisateur')
    email = request.cookies.get('email')
    
    # Vérifier si les cookies existent
    if name and email:
        # Rendre la template 'logout.html' avec les valeurs des cookies
        return render_template('logout.html', name=name, email=email)
    
    # Retourner un message si les cookies n'existent pas
    return "Aucun cookie trouvé!"

# Définir la route pour supprimer les cookies
@app.route('/delete_cookie')
def delete_cookie():
    # Créer une réponse unique et supprimer les deux cookies
    resp = make_response(redirect('/'))
    resp.delete_cookie('nom_utilisateur')
    resp.delete_cookie('email')
    
    # Retourner la réponse avec les cookies supprimés
    return resp

# Lancer l'application si le script est exécuté directement
if __name__ == '__main__':
    # Lancer l'application en mode debug
    app.run(debug=True)
