#criar as rotas do nossso site (os links)
from flask import render_template, url_for
#import o app dentro do init
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormLogin, FormCriarConta

#criar tela login-------
@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()                 #form = referencia para homepage
    return render_template("homepage.html", form=formlogin)

#tela criar conta
@app.route("/criarconta",  methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template('criarconta.html', form=formcriarconta)


@app.route("/perfil/<usuario>")#cria uma pagina para cada usuario que acessar
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


