from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#criacao do app acontece aqui
app = Flask(__name__)#nome do projeto
#criar banco dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"


database = SQLAlchemy(app)


#import o routes, que esta dentro fakepinterest
from fakepinterest import routes
