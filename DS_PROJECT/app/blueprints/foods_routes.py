from flask import Blueprint, request, jsonify
from ..models.foods import Food
from .. import db

foods_blueprint = Blueprint('foods', __name__, url_prefix='/foods')


@foods_blueprint.route('/', methods=['GET'])
def get_foods():
    foods = Food.query.all()
    return jsonify(
        [{'FoodID': f.FoodID, 'Name': f.Name, 'Carbohydrates': f.Carbohydrates, 'Protein': f.Protein, 'Fat': f.Fat} for
         f in foods])


@foods_blueprint.route('/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = Food.query.get_or_404(food_id)
    return jsonify(
        {'FoodID': food.FoodID, 'Name': food.Name, 'Carbohydrates': food.Carbohydrates, 'Protein': food.Protein,
         'Fat': food.Fat})


@foods_blueprint.route('/', methods=['POST'])
def add_food():
    data = request.json
    new_food = Food(Name=data['Name'], SupplierID=data['SupplierID'], Carbohydrates=data['Carbohydrates'],
                    Protein=data['Protein'], Fat=data['Fat'])
    db.session.add(new_food)
    db.session.commit()
    return jsonify({'message': 'Food added successfully'}), 201


@foods_blueprint.route('/<int:food_id>', methods=['PUT'])
def update_food(food_id):
    food = Food.query.get_or_404(food_id)
    data = request.json
    food.Name = data.get('Name', food.Name)
    food.Carbohydrates = data.get('Carbohydrates', food.Carbohydrates)
    food.Protein = data.get('Protein', food.Protein)
    food.Fat = data.get('Fat', food.Fat)
    db.session.commit()
    return jsonify({'message': 'Food updated successfully'})


@foods_blueprint.route('/<int:food_id>', methods=['DELETE'])
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()
    return jsonify({'message': 'Food deleted successfully'})
