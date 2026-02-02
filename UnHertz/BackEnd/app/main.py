# main.py
import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
print(f"SECRET_KEY: {SECRET_KEY}")
print(f"DATABASE_URL: {SQLALCHEMY_DATABASE_URI}")
from app.config import Config
from app.extensions import db
from sqlalchemy import text

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/db-check")
    def db_check():
        db.session.execute(text("SELECT 1"))
        return {"db": "connected"}

    return app
