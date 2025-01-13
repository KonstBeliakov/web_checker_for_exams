from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import routes  # Импорт вашего файла с маршрутами

# Создание приложения
app = Flask(__name__)

# Настройки приложения
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных
db = SQLAlchemy(app)

# Регистрация маршрутов
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
