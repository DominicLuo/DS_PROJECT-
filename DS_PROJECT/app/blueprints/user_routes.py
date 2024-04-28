from flask import Blueprint, request, jsonify
from ..models.users import User
from .. import db

user_blueprint = Blueprint('users', __name__, url_prefix='/users')


@user_blueprint.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [{'UserID': u.UserID, 'Name': u.Name} for u in users]})


@user_blueprint.route('//int:user_id', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'UserID': user.UserID, 'Name': user.Name})


@user_blueprint.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(Name=data['Name'], Address=data['Address'], Age=data['Age'], Country=data['Country'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added'}), 201


@user_blueprint.route('//int:user_id', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    user.Name = data.get('Name', user.Name)
    user.Address = data.get('Address', user.Address)
    user.Age = data.get('Age', user.Age)
    user.Country = data.get('Country', user.Country)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})


@user_blueprint.route('//int:user_id', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})


@user_blueprint.route('/active', methods=['GET'])
def get_active_users():
    # Assuming 'Active' is a boolean attribute of User
    active_users = User.query.filter_by(Active=True).all()
    return jsonify({'active_users': [{'UserID': u.UserID, 'Name': u.Name} for u in active_users]})


@user_blueprint.route('/age/int:min_age', methods=['GET'])
def get_users_by_age(min_age):
    # Filter users by minimum age
    users = User.query.filter(User.Age >= min_age).all()
    return jsonify({'users': [{'UserID': u.UserID, 'Name': u.Name} for u in users]})
