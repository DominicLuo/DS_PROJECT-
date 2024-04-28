from flask import Blueprint, request, jsonify
from ..models.products import Product
from .. import db

products_blueprint = Blueprint('products', __name__, url_prefix='/products')


@products_blueprint.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([{'ProductID': p.ProductID, 'SupplierID': p.SupplierID, 'ProductName': p.ProductName,
                     'Intro': p.Intro, 'Price': p.Price} for p in products])


@products_blueprint.route('//int:product_id', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(
        {'ProductID': product.ProductID, 'SupplierID': product.SupplierID, 'ProductName': product.ProductName,
         'Intro': product.Intro, 'Price': product.Price})


@products_blueprint.route('/', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(SupplierID=data['SupplierID'], ProductName=data['ProductName'], Intro=data.get('Intro'),
                          Price=data['Price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201


@products_blueprint.route('//int:product_id', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    data = request.json
    if 'SupplierID' in data: product.SupplierID = data['SupplierID']
    if 'ProductName' in data: product.ProductName = data['ProductName']
    if 'Intro' in data: product.Intro = data['Intro']
    if 'Price' in data: product.Price = data['Price']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})


@products_blueprint.route('//int:product_id', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})


@products_blueprint.route('/search', methods=['GET'])
def search_products():
    global products
    query = request.args.get('query')
    if query: products = Product.query.filter(Product.ProductName.ilike(f'%{query}%')).all()
    return jsonify([{'ProductID': p.ProductID, 'SupplierID': p.SupplierID, 'ProductName': p.ProductName,
                     'Intro': p.Intro, 'Price': p.Price} for p in products])


@products_blueprint.route('/price_range', methods=['GET'])
def products_by_price_range():
    min_price = request.args.get('min', type=float)
    max_price = request.args.get('max', type=float)
    products = Product.query.filter(Product.Price >= min_price, Product.Price <= max_price).all()
    return jsonify([{'ProductID': p.ProductID, 'SupplierID': p.SupplierID, 'ProductName': p.ProductName,
                     'Intro': p.Intro, 'Price': p.Price} for p in products])
