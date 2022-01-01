from enum import unique
# from logging import NullHandler, setLogRecordFactory
from flask import Flask, Blueprint, blueprints
from flask_restx import Api
from App.application import application 
from flask_swagger_ui import get_swaggerui_blueprint
from App.Admin.routes import routes
from flask_bcrypt import Bcrypt


app = Flask(__name__) # name of the flask application
# blueprint = Blueprint('Access_Control',__name__,url_prefix='/access')
app.register_blueprint(application,url_prefix= "")
app.register_blueprint(routes)
api = Api(app)
bcrypt = Bcrypt(app)

@app.route("/")
def dashboard():
    return """<h1>Access Application (SERVER)</h1>
    <h3>/swagger: swagger UI <br>
    /admin: admin apis <br>
    /admin/dashboard: admin dashboard</h3>
    """

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