from flask import Blueprint, request, jsonify
from ..models.user_level import UserLevel
from .. import db

user_level_blueprint = Blueprint('user_levels', __name__, url_prefix='/user_levels')


@user_level_blueprint.route('/', methods=['GET'])
def get_user_levels():
    user_levels = UserLevel.query.all()
    return jsonify([{'UserID': ul.UserID, 'Level': ul.Level, 'Point': ul.Point} for ul in user_levels])


@user_level_blueprint.route('//int:user_id', methods=['GET'])
def get_user_level(user_id):
    user_level = UserLevel.query.get_or_404(user_id)
    return jsonify({'UserID': user_level.UserID, 'Level': user_level.Level, 'Point': user_level.Point})


@user_level_blueprint.route('/', methods=['POST'])
def add_user_level():
    data = request.json
    new_user_level = UserLevel(UserID=data['UserID'], Level=data['Level'], Point=data['Point'])
    db.session.add(new_user_level)
    db.session.commit()
    return jsonify({'message': 'User Level added successfully'}), 201


@user_level_blueprint.route('//int:user_id', methods=['PUT'])
def update_user_level(user_id):
    user_level = UserLevel.query.get_or_404(user_id)
    data = request.json
    user_level.Level = data.get('Level', user_level.Level)
    user_level.Point = data.get('Point', user_level.Point)
    db.session.commit()
    return jsonify({'message': 'User Level updated successfully'})


@user_level_blueprint.route('//int:user_id', methods=['DELETE'])
def delete_user_level(user_id):
    user_level = UserLevel.query.get_or_404(user_id)
    db.session.delete(user_level)
    db.session.commit()
    return jsonify({'message': 'User Level deleted successfully'})


@user_level_blueprint.route('/level/int:level', methods=['GET'])
def get_users_by_level(level):
    users_at_level = UserLevel.query.filter_by(Level=level).all()
    return jsonify([{'UserID': ul.UserID, 'Level': ul.Level, 'Point': ul.Point} for ul in users_at_level])
