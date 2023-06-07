from dotenv import load_dotenv
import os

load_dotenv()

# App config
PORT = os.environ.get("PORT")
HOST = os.environ.get("HOST")
UPLOAD_FOLDER = "static/images"