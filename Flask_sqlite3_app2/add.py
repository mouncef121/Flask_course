import sqlite3



fruits = {
    "pomme": {
        "nom": "Pomme",
        "prix": 1.50,
        "description": "Fruit rouge ou vert, croquant et juteux",
        "origine": "France",
        "calories": 52
    },
    "banane": {
        "nom": "Banane",
        "prix": 0.80,
        "description": "Fruit jaune, long et courbe, doux et crémeux",
        "origine": "Costa Rica",
        "calories": 105
    },
    "orange": {
        "nom": "Orange",
        "prix": 1.20,
        "description": "Fruit orange, rond et juteux, acidulé et rafraîchissant",
        "origine": "Espagne",
        "calories": 60
    },
    "mangue": {
        "nom": "Mangue",
        "prix": 2.50,
        "description": "Fruit jaune ou orange, sucré et crémeux, avec une peau épaisse",
        "origine": "Inde",
        "calories": 55
    },
    "fraise": {
        "nom": "Fraise",
        "prix": 2.00,
        "description": "Fruit rouge, petit et sucré, avec des graines à l'extérieur",
        "origine": "France",
        "calories": 32
    },
    "kiwi": {
        "nom": "Kiwi",
        "prix": 1.80,
        "description": "Fruit vert, petit et poilu, avec une chair verte et des graines noires",
        "origine": "Nouvelle-Zélande",
        "calories": 61
    },
    "ananas": {
        "nom": "Ananas",
        "prix": 3.00,
        "description": "Fruit jaune, avec une peau épaisse et des feuilles vertes",
        "origine": "Costa Rica",
        "calories": 82
    }
}


conn = sqlite3.connect('products.db')
db = conn.cursor()

for key, value in fruits.items():
    db.execute('INSERT INTO fruits(name,price,description) VALUES(?,?,?)', (value["nom"],value["prix"],value["description"]))
    conn.commit()
   
conn.close() 