from flask import Blueprint, jsonify, request
from ..models.conferences import Conference
from .. import db

conference_blueprint = Blueprint('conferences', __name__, url_prefix='/conferences')


@conference_blueprint.route('/', methods=['GET'])
def get_conferences():
    conferences = Conference.query.all()
    return jsonify({'conferences': [
        {'ConferenceID': c.ConferenceID, 'Date': c.Date, 'Address': c.Address, 'Topic': c.Topic} for c in conferences]})


@conference_blueprint.route('//int:conference_id', methods=['GET'])
def get_conference(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    return jsonify({'ConferenceID': conference.ConferenceID, 'Date': conference.Date, 'Address': conference.Address,
                    'Topic': conference.Topic})


@conference_blueprint.route('/', methods=['POST'])
def add_conference():
    data = request.get_json()
    new_conference = Conference(Date=data['Date'], Address=data['Address'], Topic=data['Topic'])
    db.session.add(new_conference)
    db.session.commit()
    return jsonify({'message': 'Conference added'}), 201


@conference_blueprint.route('//int:conference_id', methods=['PUT'])
def update_conference(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    data = request.get_json()
    conference.Date = data.get('Date', conference.Date)
    conference.Address = data.get('Address', conference.Address)
    conference.Topic = data.get('Topic', conference.Topic)
    db.session.commit()
    return jsonify({'message': 'Conference updated successfully'})


@conference_blueprint.route('//int:conference_id', methods=['DELETE'])
def delete_conference(conference_id):
    conference = Conference.query.get_or_404(conference_id)
    db.session.delete(conference)
    db.session.commit()
    return jsonify({'message': 'Conference deleted successfully'})


@conference_blueprint.route('/search', methods=['GET'])
def search_conferences():
    global conferences
    topic = request.args.get('topic')
    if topic:  conferences = Conference.query.filter(Conference.Topic.ilike(f'%{topic}%')).all()
    return jsonify({'conferences': [
        {'ConferenceID': c.ConferenceID, 'Date': c.Date, 'Address': c.Address, 'Topic': c.Topic} for c in conferences]})
