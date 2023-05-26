from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config.from_pyfile("config.py")

@app.route("/get-query-params", methods = ["GET"])
def get_query_params():
    keyword = request.args.get("keyword")

    return {
        "keyword": keyword,
    }

@app.route("/get-path-params/<int:id>/<string:name>", methods=["GET", "POST"])
def get_path_params(id, name):
    return {
        "id": id,
        "name": "name"
    }

@app.route("/parse-request", methods = ["POST"])
def parse_request():
    return {
        "request.data: ": f"{type(request.data)}",
        "request.get_data(): ": f"{type(request.get_data())}",
        "request.get_json(): ": f"{type(request.get_json())}",
        "data": request.get_json()
    }

@app.route("/form-data-request", methods = ["POST"])
def form_data_request():
    name = request.form.get("name")
    phone = request.form.get("phone")

    return {
        "name": name,
        "phone": phone,
    }

@app.route("/upload-file", methods = ["POST"])
def upload_file():
    files = request.files.getlist("files-upload")

    data = []

    for file in files:
        pathFile = os.path.join(app.config["UPLOAD_FODER"], file.filename)
        
        data.append(f"localhost:8000/{pathFile}")
        file.save(pathFile)
    
    return jsonify(data)

if __name__ == "__main__":

    app.run(
        debug = True,
        port = 8000,
    )