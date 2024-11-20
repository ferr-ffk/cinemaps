from flask import app, render_template, request, make_response, Flask

app = Flask("cinemaps", template_folder="../templates")

@app.route("/")
def index() -> None:
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)