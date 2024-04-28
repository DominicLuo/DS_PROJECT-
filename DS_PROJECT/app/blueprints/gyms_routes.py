from flask import Blueprint, request, jsonify
from ..models.gyms import Gym
from .. import db

gyms_blueprint = Blueprint('gyms', __name__, url_prefix='/gyms')


@gyms_blueprint.route('/', methods=['GET'])
def get_gyms():
    gyms = Gym.query.all()
    return jsonify([{'GymID': gym.GymID, 'Name': gym.Name, 'Description': gym.Description} for gym in gyms])


@gyms_blueprint.route('//int:gym_id', methods=['GET'])
def get_gym(gym_id):
    gym = Gym.query.get_or_404(gym_id)
    return jsonify({'GymID': gym.GymID, 'Name': gym.Name, 'Description': gym.Description})


@gyms_blueprint.route('/', methods=['POST'])
def add_gym():
    data = request.json
    new_gym = Gym(Name=data['Name'], Description=data['Description'])
    db.session.add(new_gym)
    db.session.commit()
    return jsonify({'message': 'Gym added successfully'}), 201


@gyms_blueprint.route('//int:gym_id', methods=['PUT'])
def update_gym(gym_id):
    gym = Gym.query.get_or_404(gym_id)
    data = request.json
    gym.Name = data.get('Name', gym.Name)
    gym.Description = data.get('Description', gym.Description)
    db.session.commit()
    return jsonify({'message': 'Gym updated successfully'})


@gyms_blueprint.route('//int:gym_id', methods=['DELETE'])
def delete_gym(gym_id):
    gym = Gym.query.get_or_404(gym_id)
    db.session.delete(gym)
    db.session.commit()
    return jsonify({'message': 'Gym deleted successfully'})


@gyms_blueprint.route('/search', methods=['GET'])
def search_gyms():
    query = request.args.get('query')
    if query: gyms = Gym.query.filter(Gym.Name.ilike(f'%{query}%') | Gym.Description.ilike(f'%{query}%')).all()
