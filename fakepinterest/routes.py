#criar as rotas do nossso site (os links)
from flask import render_template, url_for, redirect
#import o app dentro do init
from fakepinterest import app, database, bcrypt
from fakepinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user
from fakepinterest.forms import FormLogin, FormCriarConta

#criar tela login-------
@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()                 #form = referencia para homepage
    return render_template("homepage.html", form=form_login)

#tela criar conta
@app.route("/criarconta",  methods=["GET", "POST"])
def criar_conta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():  #criar usuario
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,
                          senha=senha, email=form_criarconta.email.data)
        #armazenar usuario no bd
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", usuario=usuario.username)) #ao criar conta redireciona para o perfil
    return render_template('criarconta.html', form=form_criarconta)


@app.route("/perfil/<usuario>")#cria uma pagina para cada usuario que acessar
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)


