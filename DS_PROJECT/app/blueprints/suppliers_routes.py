from flask import Blueprint, request, jsonify
from ..models.suppliers import Supplier
from .. import db

suppliers_blueprint = Blueprint('suppliers', __name__, url_prefix='/suppliers')


@suppliers_blueprint.route('/', methods=['GET'])
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([{'SupplierID': s.SupplierID, 'Name': s.Name, 'Country': s.Country} for s in suppliers])


@suppliers_blueprint.route('//int:supplier_id', methods=['GET'])
def get_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    return jsonify({'SupplierID': supplier.SupplierID, 'Name': supplier.Name, 'Country': supplier.Country})


@suppliers_blueprint.route('/', methods=['POST'])
def add_supplier():
    data = request.json
    new_supplier = Supplier(Name=data['Name'], Country=data['Country'])
    db.session.add(new_supplier)
    db.session.commit()
    return jsonify({'message': 'Supplier added successfully'}), 201


@suppliers_blueprint.route('//int:supplier_id', methods=['PUT'])
def update_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    data = request.json
    supplier.Name = data.get('Name', supplier.Name)
    supplier.Country = data.get('Country', supplier.Country)
    db.session.commit()
    return jsonify({'message': 'Supplier updated successfully'})


@suppliers_blueprint.route('//int:supplier_id', methods=['DELETE'])
def delete_supplier(supplier_id):
    supplier = Supplier.query.get_or_404(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return jsonify({'message': 'Supplier deleted successfully'})


@suppliers_blueprint.route('/country/<country>', methods=['GET'])
def get_suppliers_by_country(country):
    suppliers = Supplier.query.filter_by(Country=country).all()
    return jsonify([{'SupplierID': s.SupplierID, 'Name': s.Name, 'Country': s.Country} for s in suppliers])


@suppliers_blueprint.route('/search', methods=['GET'])
def search_suppliers():
    global suppliers
    query = request.args.get('q')
    if query: suppliers = Supplier.query.filter(Supplier.Name.like(f'%{query}%')).all()
    return jsonify([{'SupplierID': s.SupplierID, 'Name': s.Name} for s in suppliers])
