# Importer les modules nécessaires de la bibliothèque Flask
from flask import Flask, render_template_string, redirect, request, url_for

# Définir une template HTML pour la page d'accueil
template='''
    <ul>
        {% for item in items%}
            <li><a href="/select/{{item}}">{{item}}</a></li>
        {%endfor%}
    </ul>

'''

# Définir une template HTML pour la page de sélection
selected = '''
<h3>Vous avez sélectionné :  {{item}} </h3>
'''

# Fonction pour créer l'application Flask
def create_app():
    # Créer une instance de l'application Flask
    app = Flask(__name__)
    
    # Définir la route pour la page d'accueil
    @app.route("/")
    def index():
        # Définir la liste des items à afficher
        items =['banana','pomme', 'carotte']
        # Rendre la template avec les items
        return render_template_string(template , items = items)
    
    # Définir la route pour la page de sélection
    @app.route("/select/<item>")
    def select_item(item):
        # Rendre la template avec l'item sélectionné
        return render_template_string(selected, item = item)
        
    # Retourner l'application créée
    return app
