from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Liste des livres
books = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "year": 1997},
    {"id": 2, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 4, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 5, "title": "A Promised Land", "author": "Barack Obama", "year": 2020}
]

# Route principale avec formulaire pour ajouter des livres
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

# Route pour ajouter un livre via POST
@app.route('/add', methods=['POST'])
def add_book():
    # Récupérer les données du formulaire ou de l'API
    title = request.form.get('title') or request.json.get('title')
    author = request.form.get('author') or request.json.get('author')
    year = request.form.get('year') or request.json.get('year')

    # Valider les données

    if not title or not author or not year:
        return "Tous les champs (title, author, year) sont obligatoires.", 400

    try:
        year = int(year)  # Vérifier que l'année est un entier
    except ValueError:
        return "L'année doit être un nombre.", 400

    # Créer un nouvel ID pour le livre
    new_id = max(book['id'] for book in books) + 1 if books else 1

    # Ajouter le livre
    new_book = {"id": new_id, "title": title, "author": author, "year": year}
    books.append(new_book)

    return jsonify(new_book), 201  # Retourner le livre ajouté avec un statut 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




















































































































'''from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def search():
	return render_template("index.html")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return f'Recherche : {query}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)'''