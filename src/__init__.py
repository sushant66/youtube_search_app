
from flask import Flask
import os
from .config import SECRET_KEY
from .database import db
from flask_msearch import Search

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)   
    app.config['SECRET_KEY'] = SECRET_KEY   #Encrypt cookies and session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['MSEARCH_INDEX_NAME'] = 'msearch'
    app.config['MSEARCH_BACKEND'] = 'whoosh'
    app.config['MSEARCH_PRIMARY_KEY'] = 'id'
    app.config['MSEARCH_ENABLE'] = True
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    from .models import Video
    

    create_database(app)
    search = Search()
    search.init_app(app)
    with app.app_context():
        search.create_index(update=True)
    return app

def create_database(app):
    if not os.path.exists('src/'+DB_NAME):
        db.create_all(app=app)
        print('Created Databse!')