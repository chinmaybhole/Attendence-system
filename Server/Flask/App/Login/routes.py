from flask import request
from App import api,create_access_token,create_refresh_token
from flask_restx import Resource,Namespace
from App.Models import User
from App.Login.serializer import *
from App.Access_Control.helper import check_userid
from passw import hash_passwd

namespace = Namespace("Login","Login with your userid and password")

class Login(Resource):

    @api.expect(login_model)
    def post(self):

        auth = request.get_json()
        if not auth or not auth["userid"] or not auth["password"]:
            print("Credetials cannot be Empty")
            return{"Error":"Credetials cannot be Empty"},401

        user,status = User(userid=auth["userid"]).getAUser("login")
        user = user[0] 
        print(user)

        if status != 200:
            return{"Error":"Could not Verify user"},401
        else:
            h_passw = hash_passwd(auth["password"])
            if h_passw == user["passw"]:
                if user["isSuperAdmin"] == 1 and user["isAdmin"] == 0 and user["isStudent"] == 0: #SuperAdmin
                    access_token = create_access_token(auth["userid"])

                    return{"access_token":access_token},200
                elif user["isSuperAdmin"] == 0 and user["isAdmin"] == 1 and user["isStudent"] == 0: #Admin
                    access_token = create_access_token(auth["userid"])

                    return{"access_token":access_token},200

                elif user["isSuperAdmin"] == 0 and user["isAdmin"] == 0 and user["isStudent"] == 0: #professor
                    access_token = create_access_token(auth["userid"])
                    
                    return{"access_token":access_token},200

                else:
                    print("Not A Valid User")
                    return{"Error":"Valid User Not Found"},404
                    
            else:
                return {"Error":"Incorrect Password"},401

namespace.add_resource(Login,"/login")
