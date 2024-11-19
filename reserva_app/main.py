from flask import app, render_template, request, make_response, Flask

app = Flask("cinemaps")

@app.route("/")
def index() -> None:
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)