from flask_restx import reqparse,fields
from App import api

access_model = api.model(
    "access_model",{
        "secrets": fields.String(),
        "timein": fields.DateTime(),
        "timeout": fields.DateTime(),
        "userid": fields.Integer(),
        "rid": fields.Integer()
    }
)