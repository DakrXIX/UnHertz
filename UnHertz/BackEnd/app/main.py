from flask import Flask
from app.extensions import db
from sqlalchemy import text

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        "postgresql://postgres:postgres@localhost:5432/unhertz"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/")
    def health():
        return {"status": "ok"}

    @app.route("/db-check")
    def db_check():
        db.session.execute(text("SELECT 1"))
        return {"db": "connected"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)