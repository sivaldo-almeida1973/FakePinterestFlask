from flask import Flask
#criacao do app

app = Flask(__name__)#nome do projeto


from fakepinterest import routes
