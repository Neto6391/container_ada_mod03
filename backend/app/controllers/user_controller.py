from flask import Blueprint, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('usuarios', __name__)
user_service = UserService()

@user_bp.route('/', methods=['GET'])
def get_all_users():
    users = user_service.get_all_users()
    return jsonify(users), 200
