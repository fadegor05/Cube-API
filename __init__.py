from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

from database import db
from views import main


def make_app(config_file = 'settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(main)
    app.run()
    return app


if __name__ == '__main__':
    make_app()