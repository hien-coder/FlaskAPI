from flask import Flask, render_template
from view import users_view, upload_view
from utils import config

app = Flask(__name__, template_folder="template")
app.config.from_object(config)

@app.route("/")
def home():
    return render_template("home.html")

# Blueprint
app.register_blueprint(users_view)
app.register_blueprint(upload_view)

if __name__ == "__main__":

    app.run (
        debug = True,
        port = app.config["PORT"],
        host = app.config["HOST"]
    )