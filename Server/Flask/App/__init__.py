from enum import unique
import sqlite3
# from logging import NullHandler, setLogRecordFactory
from flask import Flask, Blueprint, blueprints
from flask_restx import Api
from flask_swagger_ui import get_swaggerui_blueprint
# from App.Admin.routes import routes



# app = Flask(__name__) # name of the flask application
blueprint = Blueprint('Access_Control',__name__,url_prefix='/access')
api = Api(blueprint)

def create_app():
    app = Flask(__name__)
     
    main = Blueprint('main', __name__)

    @main.route('/')
    def index():
        return """<h1>Access Application (SERVER)</h1>
        <h3>/access: swagger UI <br>"""  

    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Seans-Python-Flask-REST-Boilerplate"
        }
    )

    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

    from App.Admin.routes import namespace as Admin
    api.add_namespace(Admin)
    # app.register_blueprint(routes)
    app.register_blueprint(blueprint)   
    app.register_blueprint(main) 

    return app    