from pathlib import Path

from flask import Flask
from flask_cors import CORS

from app.controller import app as bp_main


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=f"{(Path(__file__).parent.parent / 'templates').resolve()}",
        static_folder=f"{(Path(__file__).parent.parent / 'static').resolve()}",
    )
    CORS(app)
    app.register_blueprint(bp_main)
    return app
