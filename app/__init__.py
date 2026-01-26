from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Blueprint'leri kaydet
    from app.main import main_bp
    app.register_blueprint(main_bp)
    
    from app.auth import auth_bp
    app.register_blueprint(auth_bp)
    
    return app