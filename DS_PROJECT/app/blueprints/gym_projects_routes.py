from flask import Blueprint, request, jsonify
from ..models.gym_projects import GymProject
from .. import db

gym_projects_blueprint = Blueprint('gym_projects', __name__, url_prefix='/gym_projects')


@gym_projects_blueprint.route('/', methods=['GET'])
def get_gym_projects():
    projects = GymProject.query.all()
    return jsonify([{'ProjectID': project.ProjectID, 'Projectname': project.Projectname, 'Duration': project.Duration,
                     'Frequency': project.Frequency} for project in projects])


@gym_projects_blueprint.route('//int:project_id', methods=['GET'])
def get_gym_project(project_id):
    project = GymProject.query.get_or_404(project_id)
    return jsonify({'ProjectID': project.ProjectID, 'Projectname': project.Projectname, 'Duration': project.Duration,
                    'Frequency': project.Frequency})


@gym_projects_blueprint.route('/', methods=['POST'])
def add_gym_project():
    data = request.json
    new_project = GymProject(Projectname=data['Projectname'], Duration=data['Duration'], Frequency=data['Frequency'])
    db.session.add(new_project)
    db.session.commit()
    return jsonify({'message': 'Gym Project added successfully'}), 201


@gym_projects_blueprint.route('//int:project_id', methods=['PUT'])
def update_gym_project(project_id):
    project = GymProject.query.get_or_404(project_id)
    data = request.json
    project.Projectname = data.get('Projectname', project.Projectname)
    project.Duration = data.get('Duration', project.Duration)
    project.Frequency = data.get('Frequency', project.Frequency)
    db.session.commit()
    return jsonify({'message': 'Gym Project updated successfully'})


@gym_projects_blueprint.route('//int:project_id', methods=['DELETE'])
def delete_gym_project(project_id):
    project = GymProject.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return jsonify({'message': 'Gym Project deleted successfully'})


@gym_projects_blueprint.route('/duration/int:duration', methods=['GET'])
def get_gym_projects_by_duration(duration):
    projects = GymProject.query.filter_by(Duration=duration).all()
    return jsonify([{'ProjectID': project.ProjectID, 'Projectname': project.Projectname, 'Duration': project.Duration,
                     'Frequency': project.Frequency} for project in projects])


@gym_projects_blueprint.route('/frequency/int:frequency', methods=['GET'])
def get_gym_projects_by_frequency(frequency):
    projects = GymProject.query.filter_by(Frequency=frequency).all()
    return jsonify([{'ProjectID': project.ProjectID, 'Projectname': project.Projectname, 'Duration': project.Duration,
                     'Frequency': project.Frequency} for project in projects])
