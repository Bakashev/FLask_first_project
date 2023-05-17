from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Инициализация приложения
app = Flask(__name__, template_folder='templates')

# # Создаем DSN для СУБД в конфигурации Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

#Обязательно для работы не выкладывать его на GIT
app.secret_key='13412938123095812360589613'

# Создаем объект для работы с SQLAlchemy
db = SQLAlchemy(app)
