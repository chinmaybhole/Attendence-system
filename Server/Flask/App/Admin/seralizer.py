from flask_restx import reqparse,fields
from App import api
from App.Admin.helper import custom_validation_parser

user_parser = reqparse.RequestParser()
user_parser.add_argument('userid', help='Enter Userid for eg 222....', type=custom_validation_parser, location='args')
