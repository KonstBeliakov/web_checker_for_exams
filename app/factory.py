from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Создаём объект расширения, но не привязываем к приложению


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Привязываем SQLAlchemy к приложению

    # Регистрация Blueprints
    from app.routes import routes
    app.register_blueprint(routes)

    return app
