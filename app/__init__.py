from flask import Flask
from app.web.book import web
from app.models.book import db


def creat_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    app.register_blueprint(web)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
