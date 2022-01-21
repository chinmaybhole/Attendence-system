from flask_restx import reqparse,fields
from App import api

user_parser = reqparse.RequestParser()
user_parser.add_argument('userid', help='Enter Userid for eg 222....', required= False)

room_parser = reqparse.RequestParser()
room_parser.add_argument('roomno', help='Enter roomno for eg 801', required= False)

super_admin_login_parser = api.parser()
super_admin_login_parser.add_argument("userid",location = "headers", help= "Enter your userid", required = "True")
super_admin_login_parser.add_argument("passw",location = "headers", help= "Enter your password", required = "True")

super_post_user = api.model(
    "post_user",{
        "userid": fields.Integer(),
        "fname": fields.String(),
        "lname": fields.String(),
        "passw" : fields.String(),
        "rollno" : fields.Integer(),
        "div": fields.String(),
        "dept": fields.String(),
        "phone": fields.Integer(),
        "isStudent": fields.Integer(),
        "isAdmin": fields.Integer()
    }
)

super_put_user = api.model(
    "put_user",{
        "userid": fields.Integer(),
        "fname": fields.String(),
        "lname": fields.String(),
        "passw" : fields.String(),
        "rollno" : fields.Integer(),
        "div": fields.String(),
        "dept": fields.String(),
        "phone": fields.Integer(),
        "isAdmin": fields.Integer()
    }
)

super_delete_user = api.model(
    "delete_user",{
        "userid": fields.Integer()
    }
)

super_post_room = api.model(
    "post_room",{
        "roomno": fields.Integer(),
        "roomname": fields.String()
    }
)

super_delete_room = api.model(
    "delete_room",{
        "roomno": fields.Integer()
    }
)

auth_failures = {
	401 : "Credentials Incorrect",
    404 : "User not found",
    500 : "Internal Server Error"
}