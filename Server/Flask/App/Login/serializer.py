from App import api
from flask_restx import fields

login_model = api.model(
    "login_model",{
        "userid":fields.String(),
        "password":fields.String()
    }
)