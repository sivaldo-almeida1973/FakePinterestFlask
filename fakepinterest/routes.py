#criar as rotas do nossso site (os links)
from flask import render_template, url_for
#import o app dentro do init
from fakepinterest import app
from flask_login import login_required


#criar servidor local/rota/homepage
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/perfil/<usuario>")#cria uma pagina para cada usuario que acessar
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


