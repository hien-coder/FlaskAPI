import os
from dotenv import load_dotenv

load_dotenv()

# App config
SECRET_KEY = os.environ.get("KEY")
PORT = os.environ.get("PORT")
HOST = os.environ.get("HOST")

# DB config
DB_USER = os.environ("DB_USER")
DB_PASSWORD = os.environ("DB_PASSWORD")
DB_HOST = os.environ("DB_HOST")
DB_NAME = os.environ("DB_NAME")

SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

