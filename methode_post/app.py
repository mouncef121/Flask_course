# Importer les modules nécessaires de la bibliothèque Flask
from flask import Flask, render_template, request, redirect, url_for

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir un dictionnaire pour mapper les couleurs en anglais vers les couleurs en français
colors = {
    'blue' : 'bleu',
    'green' : 'vert',
    'yellow' : 'jaune',
    'red' : 'rouge',
    'black' : 'noir'
}

# Définir la route pour la page d'accueil
@app.route('/', methods=['GET', 'POST'])
def index():
    # Vérifier si la méthode de requête est GET
    if request.method == 'GET':
        # Rendre la template 'index.html' pour la page d'accueil
        return render_template('index.html')
    else : 
        # Afficher un message pour indiquer que le formulaire a été soumis
        print("Form submited!")
        # Récupérer la valeur de la couleur sélectionnée à partir du formulaire
        color = str(request.form.get('color'))
        # Rendre la template 'color.html' avec la couleur sélectionnée et sa traduction en français
        return render_template('color.html', colorstyle = color, Color = colors[color])

# Lancer l'application si le script est exécuté directement
if __name__ == '__main__':
    # Lancer l'application en mode debug
    app.run(debug=True)
