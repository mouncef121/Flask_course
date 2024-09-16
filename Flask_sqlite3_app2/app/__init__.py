from flask import Flask, render_template, request,url_for, redirect, session
import sqlite3
from flask_session import Session



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mykey'
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/registrants', methods=['POST', 'GET'])
    def i_register():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            conn = sqlite3.connect('registrant1.db')
            db = conn.cursor()
            db.execute("SELECT email FROM users")
            emails = [row[0] for row in db.fetchall()]
            if email not in emails:
                db.execute('INSERT INTO users(email, password) VALUES (?,?)', (email, password))
                conn.commit()
                conn.close()
                return redirect(url_for('registrant', email=email))
            else:
                conn.close()
                return render_template('register.html', error='Email already exists')
        return "error"

    @app.route('/registrantinfo/<email>')
    def registrant(email):
        conn = sqlite3.connect('registrant1.db')
        db = conn.cursor()
        db.execute('SELECT email FROM users WHERE email = ?', (email,))
        result = db.fetchone()
        conn.close()
        if result:
            return render_template('registrants.html', email=email)
        else:
            return "error"

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/loged', methods=['POST'])
    def loged():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            conn = sqlite3.connect('registrant1.db')
            db = conn.cursor()
            db.execute("SELECT email, password FROM users WHERE email = ?", (email,))
            user = db.fetchone()
            conn.close()
            if user and user[1] == password: # modifier l'index de 2 à 1
                session['email'] = email #stocker l'email dans la session
                return render_template('loged.html', Email= user[0]) # modifier l'index de 1 à 0
            return render_template('login.html', error='Invalid email or password')
        return redirect('register.html')
    
    @app.route('/logout')
    def logout():
        session.clear()
        return render_template("login.html")
        
    
    @app.route("/products")
    def product():
        conn = sqlite3.connect('products.db')
        try:
            db= conn.cursor()
            db.execute('SELECT * FROM fruits;')
            fruits = db.fetchall()
        finally:
            conn.close()
        
        return render_template('products.html', products = fruits)
    

    @app.route('/add_to_cart', methods =["POST"])
    def add_to_cart():
        id_p = request.form.get('id')
        
        conn = sqlite3.connect('products.db')
        try :
            db = conn.cursor()
            db.execute('SELECT * FROM fruits  WHERE id = ?', (id_p,))
            fruit = db.fetchone()
        finally:
            conn.close()
        
        #ajouter produit au le panier
        if 'cart' not in session :
            session['cart'] = []
            
        # Vérifier si le produit est déjà dans le panier
        if fruit not in session['cart']:
            session['cart'].append(fruit)
        
        return redirect('/cart')
    
    @app.route('/cart')
    def cart():
        if 'email' in session:
            email = session['email']
            if 'cart' in session:
                return render_template('cart.html', cart = session['cart'], email = email)
            return render_template('cart.html', cart=[])
        return redirect('/login')
        

    
    @app.route('/remove', methods =["POST"])
    def remove():
        id_p = request.form.get('id')
        if 'cart' in session:
            session['cart'] = [fruit for fruit in session['cart'] if str(fruit[0])!=id_p]
        return redirect('/cart')
    
    
    return app
