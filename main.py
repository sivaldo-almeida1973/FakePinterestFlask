from flask import Flask

app = Flask(__name__)#nome do projeto

#criar servidor local/rota/homepage
@app.route("/")
def homepage():
    return "FakePinterest - Meu primeiro site no ar!"

#colocar site no ar
if __name__ == "__main__":
      app.run(debug=True) #qualuqer alteração que faça , atualiza


