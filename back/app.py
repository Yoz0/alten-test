from flask import Flask, request, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):
    id : int
    code : str
    name : str
    description : str
    image : str
    price : int
    category : str
    quantity : int
    inventoryStatus : str
    rating : int

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(100))
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    image = db.Column(db.String(100))
    price = db.Column(db.Integer)
    category = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    inventoryStatus = db.Column(db.String(100))
    rating = db.Column(db.Integer)

with app.app_context():
    db.drop_all()
    db.create_all()
    json_data = json.load(open("products.json"))
    for json_prod in json_data["data"]:
        prod = Product()
        for key, value in json_prod.items():
            setattr(prod, key, value)
        db.session.add(prod)
    db.session.commit()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products", methods=['GET'])
def products():
    with app.app_context():
        prods = Product.query.all()
        return jsonify(prods)

@app.route("/products", methods=['POST'])
def create_product():
    new_prod = request.get_json()
    with app.app_context():
        prod = Product()
        for key, value in new_prod.items():
            setattr(prod, key, value)
        db.session.add(prod)
        db.session.commit()
        return jsonify(prod)

@app.route("/products/<id>", methods=['GET'])
def get_product(id):
    with app.app_context():
        prod = Product.query.get(int(id))
        return jsonify(prod)

@app.route("/products/<id>", methods=['PATCH'])
def patch_product(id):
    new_prod = request.get_json()
    with app.app_context():
        prod = Product.query.get(int(id))
        for key, value in new_prod.items():
            setattr(prod, key, value)
        db.session.commit()
        return jsonify(prod)

@app.route("/products/<id>", methods=['DELETE'])
def delete_product(id):
    with app.app_context():
        prod = Product.query.get(int(id))
        db.session.delete(prod)
        db.session.commit()
        return jsonify(prod)
