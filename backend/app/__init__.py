# Backend code Flask app start
# Actualización de código con comentarios incluídos
# Recuerden actualizar commits
# FRONT NO TOCAR BACKEND

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf import CSRFProtect
from config import Config 

# Inicialización de las extenciones

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicio de la extención de aplicación

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)

    # REgistro de blueprints

    from app.routes.auth import bp as auth_bp
    from app.routes.user import bp as user_bp
    from app.routes.transactions import bp as transaction_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(transaction_bp)


    return app
