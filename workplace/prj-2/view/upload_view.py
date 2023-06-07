import os
from flask import Blueprint, render_template, request
from utils.config import UPLOAD_FOLDER

upload_view = Blueprint("upload_view", __name__)

@upload_view.route("/upload-file", methods=["GET", "POST"])
def upload_file():
    try:
        if request.method == "GET":
            return render_template("upload_file.html")
        else:
            file = request.files.get("file")

            if file is not None and file.filename != "":
                path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(path)

                return render_template("upload_file.html", pathfile = path)
            else:
                return "Error"
            
    except Exception as E:
        return f"Error: {E}"