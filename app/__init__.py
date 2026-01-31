from flask import Flask
from flask_login import LoginManager
from sqlalchemy.exc import OperationalError
from config import config
from app.models import db, User

login_manager = LoginManager()
login_manager.login_view = 'auth.login' # Giriş yapmamış kullanıcıların yönlendirileceği sayfa

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)
    login_manager.init_app(app)

    # Otomatik Tablo Oluşturma Mantığı
    with app.app_context():
        try:
            db.create_all()
        except OperationalError:
            pass
    
    from app.main.routes import main_bp
    app.register_blueprint(main_bp)
    
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)
    
    return app