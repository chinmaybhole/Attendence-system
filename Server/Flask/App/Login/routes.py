from flask import request
from App import api,create_access_token,create_refresh_token
from flask_restx import Resource,Namespace
from App.Models import User
from App.Login.serializer import *
from Server.Flask.App.Access_Control.helper import check_userid

namespace = Namespace("Login","Login with your userid and password")

class Login(Resource):

    @api.expect(login_model)
    def post(self):

        auth = request.get_json()
        if not auth or not auth["userid"] or not auth["password"]:
            print("Credetials cannot be Empty")
            return("Credetials cannot be Empty"),401

        user,status = User(userid=auth["userid"]).getAUser("login")  

        if status != True:
            return("Could not Verify user"),401

        
        
        print(auth)

namespace.add_resource(Login,"/login")
