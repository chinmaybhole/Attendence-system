from flask_restx import reqparse,fields
from App import api

post_access = api.model(
    "post_access",{
        "timein": fields.DateTime(),
        "timeout": fields.DateTime(),
        "userid": fields.Integer(),
        "profid": fields.Integer(),
        "rid": fields.Integer()
    }
)