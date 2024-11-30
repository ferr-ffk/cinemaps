from flask import app, render_template, request, make_response, Flask, redirect, url_for

app = Flask("cinemaps", template_folder="../templates")

@app.route("/")
def index():
    return render_template("index.html")


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