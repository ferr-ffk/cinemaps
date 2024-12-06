from flask import app, render_template, request, make_response, Flask, redirect, url_for, session

app = Flask("cinemaps", template_folder="../templates", static_folder="../static")

app.config['SECRET_KEY'] = '\xc3$Fg+\xeb\xb4T\xa4\x19~\xf1$\xbd_}^A\xfcOA_\x9c\xfb\xa3\xcbK\x05\xb9W\xe3\x04'


@app.route("/debug/sessao")
def exibir_sessao():
    s = ''
    
    for key in session:
        s = s + key + ": " + session[key] + "\n"
    
    return s


@app.route("/debug/limpar-sessao")
def limpar_sessao():
    session.clear()
    
    return redirect(url_for(index.__name__))

@app.route("/")
def index():
    print(session)
    
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=['post'])
def login_post():
    # Verificar se nome de usuário ou senha são válidos
    
    # Adicionar à sessão
    # Pegar id do usuário no banco
    usuario = {
        "email": request.form['email'],
        "usuario": "nome_usuario_obtido_do_banco",
    }
    
    for key in usuario:
        session[key] = usuario[key]
    
    return redirect(url_for(index.__name__))


@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")


@app.route("/cadastro", methods=['post'])
def cadastro_post():
    usuario = {
        "usuario": request.form['usuario'],
        "email": request.form['email'],
        "senha": request.form['senha'],
    }
    
    # Criar usuário no banco usando o fetch
    
    # Adicionar à sessão
    for key in usuario:
        session[key] = usuario[key]
    
    return redirect(url_for(index.__name__))


@app.route("/cinemas/<int:cinema>")
def cinema(cinema: int):
    return render_template("cinema.html", cinema=cinema)


@app.route("/cinemas")
def cinemas():
    return "Cinemas"


@app.route("/filmes")
def filmes():
    return "Filmes"


@app.route("/filmes/<int:filme>")
def filme(filme: int):
    return "Filme {}".format(filme)


@app.errorhandler(404)
def nao_encontrado(e):
    return "A página {} não foi encontrada! Voltar para a principal <a href=\"/\">por aqui</a>".format(request.path), 404


if __name__ == "__main__":
    app.run(debug=True)
