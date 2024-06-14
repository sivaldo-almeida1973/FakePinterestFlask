from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


#criacao do app acontece aqui
app = Flask(__name__)#nome do projeto
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SECRET_KEY"] = "a73862f42afd78ba024a89e89b291685"

#criar banco dados
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


#import o routes, que esta dentro fakepinterest
from fakepinterest import routes
