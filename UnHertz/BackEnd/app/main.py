from flask import Flask
from app.config import Config
from app.extensions import db
from sqlalchemy import text
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    @app.route("/db-check")
    def db_check():
        db.session.execute(text("SELECT 1"))
        return {"db": "connected"}

    return app
