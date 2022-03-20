from flask import Flask, Blueprint, request, blueprints
from flask_restx import Api
from App import Models
from functools import wraps
import jwt

from config import Config ,ACCESS_EXPIRES, REFRESH_EXPIRES

blueprint = Blueprint('Access_Control',__name__,url_prefix='/access')
api = Api(blueprint)
app = Flask(__name__)


def create_app(config_class = Config):

    app.config.from_object(Config)
     
    main = Blueprint('main', __name__)

    @main.route('/')
    def index():
        return """<h1>Access Application (SERVER)</h1>
        <h3>/access: swagger UI <br>"""


    from App.Admin.routes import namespace as Admin
    from App.SuperAdmin.routes import namespace as SuperAdmin
    from App.Professor.routes import namespace as Professor
    from App.Access_Control.routes import namespace as Access
    from App.Login.routes import namespace as Login

    api.add_namespace(Login)
    api.add_namespace(Access)
    api.add_namespace(Admin)
    api.add_namespace(SuperAdmin)
    api.add_namespace(Professor)

    # app.register_blueprint(routes)
    app.register_blueprint(blueprint)   
    app.register_blueprint(main) 

    return app

def create_access_token(uid):

    access_token = jwt.encode({
        "user": uid,
        "exp": ACCESS_EXPIRES
    },app.config["SECRET_KEY"],algorithms=["HS256"])

    return access_token

def create_refresh_token(uid):

    refresh_token = jwt.encode({
        "user": uid,
        "exp": REFRESH_EXPIRES
    },app.config["SECRET_KEY"],algorithms=["HS256"])

    return refresh_token

def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
    
        if not token:
            return {'message': 'a valid token is missing'}
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = Models.User(userid=data['user'])
        except:
            return {'message': 'token is invalid'}
    
        return f(data, *args, **kwargs)
    return decorator
