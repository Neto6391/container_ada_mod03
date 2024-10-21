from flask import Blueprint, request, jsonify, abort
from app.services.event_service import EventService

event_bp = Blueprint('eventos', __name__)
event_service = EventService()

@event_bp.route('/', methods=['GET'])
def get_all_events():
    events = event_service.get_all_events()
    return jsonify(events), 200

@event_bp.route('/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    if event_service.delete_event(event_id):
        return jsonify({"message": f"Evento com ID {event_id} foi deletado com sucesso"}), 200
    else:
        abort(404, description="Evento não encontrado")

@event_bp.route('/', methods=['POST'])
def add_event():
    event_data = request.get_json()

    required_fields = ['titulo', 'data', 'horario', 'preco', 'url_da_imagem', 'evento_privado']
    if not all(field in event_data for field in required_fields):
        return jsonify({"error": "Faltam campos obrigatórios"}), 400

    new_event = event_service.add_event(event_data)
    
    return jsonify(new_event), 201