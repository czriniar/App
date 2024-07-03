from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1001010101010101101'
    from .views import views

    app.register_blueprint(views, url_prefix='/')
    
    return app
