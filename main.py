from flask import Flask, render_template

app = Flask(__name__)#nome do projeto

#criar servidor local/rota/homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

#colocar site no ar
if __name__ == "__main__":
      app.run(debug=True) #qualuqer alteração que faça , atualiza


