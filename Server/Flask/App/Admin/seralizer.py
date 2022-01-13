from flask_restx import reqparse,fields
from App import api
from App.Admin.helper import custom_validation_parser

user_parser = reqparse.RequestParser()
user_parser.add_argument('userid', help='Enter Userid for eg 222....', required= False)


post_user = api.model(
    "post_user",{
        "userid": fields.Integer(),
        "fname": fields.String(),
        "lname": fields.String(),
        "passw" : fields.String(),
        "rollno" : fields.Integer(),
        "div": fields.String(),
        "dept": fields.String(),
        "phone": fields.Integer(),
        "isStudent": fields.Integer()
    }
)

put_user = api.model(
    "put_user",{
        "userid": fields.Integer(),
        "fname": fields.String(),
        "lname": fields.String(),
        "passw" : fields.String(),
        "rollno" : fields.Integer(),
        "div": fields.String(),
        "dept": fields.String(),
        "phone": fields.Integer()
    }
)

delete_user = api.model(
    "delete_user",{
        "userid": fields.Integer()
    }
)