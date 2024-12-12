from flask import app, render_template, request, make_response, Flask, redirect, url_for, session, flash
import requests

from cinemaps.validacao import *
from service.usuario import *
from util.sql import criar_banco_cinemaps

app = Flask("cinemaps", template_folder="../templates", static_folder="../static")

app.config['SECRET_KEY'] = '\xc3$Fg+\xeb\xb4T\xa4\x19~\xf1$\xbd_}^A\xfcOA_\x9c\xfb\xa3\xcbK\x05\xb9W\xe3\x04'


criar_banco_cinemaps()


@app.route("/sair")
def sair():
    session.clear()
    
    flash("Sessão encerrada.")
    
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
    # Pegar id do usuário no banco
    usuarios_com_id = select_from_tabela_por_condicao('usuario', f'WHERE email = \'{request.form['email']}\'')
    
    usuario_existe = len(usuarios_com_id) > 0
    
    if not usuario_existe:
        erro = "Usuário não encontrado. Certifique-se de que o email foi digitado corretamente."
        
        return render_template("login.html", erro=erro, tipo_erro="warning")
    
    usuario = usuarios_com_id[0]
    
    if usuario['senha'] != request.form['senha']:
        erro = "Senha incorreta. Tente novamente."
        
        return render_template("login.html", erro=erro, tipo_erro="danger")
    
    usuario_sessao = {
        "email": usuario['email'],
        "usuario": usuario['usuario']
    }
    
    # Adicionar à sessão
    for key in usuario_sessao:
        session[key] = usuario[key]
    
    return redirect(url_for(index.__name__))


@app.route("/cadastro")
def cadastro():
    # Limita o usuário a fazer outro cadastro com sua conta já logada
    if session:
        flash("Conta já criada! Encerre sua sessão para prosseguir para a tela de cadastro.")
        
        return redirect(url_for(index.__name__))
    
    return render_template("cadastro.html")


@app.route("/cadastro", methods=['post'])
def cadastro_post():
    erro = None
    
    # Verificar se nome de usuário ou senha são válidos
    if not nome_usuario_valido(request.form['usuario']):
        erro = "Nome de usuário invalido! Certifique-se que tem entre 6 e 16 caracteres e não inicia ou termina com números."
        
        return render_template("cadastro.html", erro=erro, tipo_erro="warning")
        
        
    if not senha_valida(request.form['senha'], request.form['senha-confirmar']):
        erro = "Senha inválida! Verifique se os campos são iguais e possui no mínimo de oito caracteres, ao menos uma letra, um número e um caractere especial"
        
        return render_template("cadastro.html", erro=erro, tipo_erro="warning")
    
    
    if not email_valido(request.form['email']):
        erro = "Email inválido! Digite um email válido para continuar."
        
        return render_template("cadastro.html", erro=erro, tipo_erro="danger")
        
        
    usuario = {
        "usuario": request.form['usuario'],
        "email": request.form['email'],
        "senha": request.form['senha'],
    }

    # Criar usuário no banco usando o fetch
    requests.post(request.url_root + "api/usuarios", headers=usuario)
    
    flash("Conta criada com sucesso!")

    # Adicionar à sessão
    for key in usuario:
        session[key] = usuario[key]

    return redirect(url_for(index.__name__))
    

@app.route("/formulario_db")
def pagina_criar_db():
    return render_template("formulario_db.html")    


@app.route("/formulario_db", methods=['post'])
def pagina_criar_db_post():
    resp = make_response(redirect(url_for(index.__name__)))
    
    for field in request.form:
        resp.set_cookie(field, request.form[field])

    return resp


@app.route("/cookies")
def pagina_get_cookies():
    c = [
        request.cookies.get('host'),
        request.cookies.get('usuario'),
        request.cookies.get('banco'),
        request.cookies.get('senha')
    ]

    return str(c)


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


@app.route("/api/cinemas")
def api_cinemas():
    return [
        {
            "id": 1,
            "nome": "tal"
        },
        {
            "id": 2,
            "nome": "x"
        },
        {
            "id": 3,
            "nome": "y"
        },
        {
            "id": 4,
            "nome": "z"
        }
    ]


@app.route("/api/usuarios", methods=['post', 'get'])
def api_usuarios():
    usuario = {
        "usuario": request.headers.get("usuario"),
        "senha": request.headers.get("senha"),
        "email": request.headers.get("email"),
        "apelido": ""
    }

    UsuarioService.criar_usuario(usuario)

    return redirect(url_for(index.__name__))


@app.errorhandler(404)
def nao_encontrado(e):
    return "A página {} não foi encontrada! Voltar para a principal <a href=\"/\">por aqui</a>".format(request.path), 404


if __name__ == "__main__":
    app.run(debug=True)
