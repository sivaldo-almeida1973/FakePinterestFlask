from flask import Flask, render_template, url_for

app = Flask(__name__)#nome do projeto

#criar servidor local/rota/homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/perfil/<usuario>")#cria uma pagina para cada usuario que acessar
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


#colocar site no ar
if __name__ == "__main__":
      app.run(debug=True) #qualuqer alteração que faça , atualiza


