from flask import Flask, Blueprint, request, blueprints
from flask_restx import Api
from functools import wraps
from App import Models
from config import Config ,ACCESS_EXPIRES, REFRESH_EXPIRES
import jwt

blueprint = Blueprint('Access_Control',__name__,url_prefix='/access')
api = Api(blueprint)

def create_app(config_class = Config):
    app = Flask(__name__)

    app.config.from_object(Config)
     
    main = Blueprint('main', __name__)

    @main.route('/')
    def index():
        return """<h1>Access Application (SERVER)</h1>
        <h3>/access: swagger UI <br>"""

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



    from App.Admin.routes import namespace as Admin
    from App.SuperAdmin.routes import namespace as SuperAdmin
    from App.Professor.routes import namespace as Professor
    api.add_namespace(Admin)
    api.add_namespace(SuperAdmin)
    api.add_namespace(Professor)

    # app.register_blueprint(routes)
    app.register_blueprint(blueprint)   
    app.register_blueprint(main) 

    return app