from flask import Flask
from flask_login import LoginManager
from app.models.book import db
from flask_mail import Mail
from flask_cache import Cache


login_manager = LoginManager()

def creat_app():
    app = Flask(__name__)
    app.config.from_object('app.setting')
    app.config.from_object('app.secure')
    register_blueprint(app)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    from app.web.book import web
    from app.web import web
    app.register_blueprint(web)
