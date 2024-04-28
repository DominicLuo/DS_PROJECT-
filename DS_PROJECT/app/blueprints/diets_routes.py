from flask import Blueprint, request, jsonify
from ..models.diets import Diet
from .. import db

diets_blueprint = Blueprint('diets', __name__, url_prefix='/diets')

@diets_blueprint.route('/', methods=['GET'])
def get_diets():
    diets = Diet.query.all()
    return jsonify([{'DietID': d.DietID, 'Name': d.Name, 'Description': d.Description} for d in diets])

@diets_blueprint.route('/<int:diet_id>', methods=['GET'])
def get_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    return jsonify({'DietID': diet.DietID, 'Name': diet.Name, 'Description': diet.Description})

@diets_blueprint.route('/', methods=['POST'])
def add_diet():
    data = request.json
    new_diet = Diet(Name=data['Name'], Description=data['Description'])
    db.session.add(new_diet)
    db.session.commit()
    return jsonify({'message': 'Diet added successfully'}), 201

@diets_blueprint.route('/<int:diet_id>', methods=['PUT'])
def update_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    data = request.json
    diet.Name = data.get('Name', diet.Name)
    diet.Description = data.get('Description', diet.Description)
    db.session.commit()
    return jsonify({'message': 'Diet updated successfully'})

@diets_blueprint.route('/<int:diet_id>', methods=['DELETE'])
def delete_diet(diet_id):
    diet = Diet.query.get_or_404(diet_id)
    db.session.delete(diet)
    db.session.commit()
    return jsonify({'message': 'Diet deleted successfully'})
