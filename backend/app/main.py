from flask import Flask
from flask_cors import CORS
from app.controllers.event_controller import event_bp
from app.controllers.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.register_blueprint(event_bp, url_prefix='/eventos')
    app.register_blueprint(user_bp, url_prefix='/usuarios')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 3000)))
