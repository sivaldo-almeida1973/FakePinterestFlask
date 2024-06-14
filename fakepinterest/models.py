#criar a estrutura do banco de dados
from fakepinterest import database
from datetime import datetime

#criar tabelas-------------
class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=True)
    email = database.Column(database.String, nullable=True, unique=True)
    senha = database.Column(database.String, nullable=True)
    fotos = database.Relationship("Foto", backref="usuario", lazy=True)


#foto precisa relacionar/ usuario(id_usuario)
class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    imagem = database.Column(database.String, default="default.png")
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
