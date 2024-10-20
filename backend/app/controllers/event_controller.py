from flask import Blueprint, jsonify
from app.services.event_service import EventService

event_bp = Blueprint('eventos', __name__)
event_service = EventService()

@event_bp.route('/', methods=['GET'])
def get_all_events():
    events = event_service.get_all_events()
    return jsonify(events), 200
