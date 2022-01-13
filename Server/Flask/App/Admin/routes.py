from sqlite3.dbapi2 import Error
from flask import Blueprint,request
from flask.wrappers import Response
from App import Models, api
from flask_restx import Resource,reqparse,Namespace
from App.Admin.seralizer import *
from App.Admin.helper import *
from passw import hash_passwd

users = Models.User()
rooms = Models.Rooms()
ac = Models.Access_Control()
logs = Models.Logs()

# routes = Blueprint("routes",__name__)

namespace = Namespace('Admin', description= "All About Admin API's")


class User(Resource):
    # get all data
    @api.doc(responses={
        200 : "Success",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(user_parser)
    def get(self):
        try:
            body = request.args
            if "userid" in body:
                check = check_userid(body["userid"],"get") 
                if check[-1] == 200:
                    usr = Models.User(body["userid"])
                    u = usr.getAUser()
                    return {"user":u},200
                else:
                    return{"message": check},404
            else:
                u=users.getAllUsers()
                a= ac.getAllACData()
                r= rooms.getAllRooms()
                l = logs.getAllLogs()
                return {'User':u,"Access_Control":a,"Rooms":r,"Logs":l},200
            
        except Exception as e:
            print(str(e))

    # post user data
    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(post_user)
    def post(self):
        try:
            
            body = request.get_json()
            userid = check_userid(body["userid"])
            phoneno = check_phoneno(body["phone"])
            h_passw = hash_passwd(body["passw"])  # hashing the password
            if userid == True and phoneno == True:
                if body["rollno"] == 0 and body["div"] == "None":
                    rollno = None
                    div = None
                    user = Models.User(body["userid"],body["fname"],body["lname"],h_passw,rollno,div,body["dept"],body["phone"],body["isStudent"])
                    response = user.insert_user()

                    return {
                        "message": response
                    }    

                else:
                    user = Models.User(body["userid"],body["fname"],body["lname"],h_passw,body["rollno"],body["div"],body["dept"],body["phone"],body["isStudent"])
                    response = user.insert_user()

                    return {
                        "message": response
                    } 
            else:
                return userid

            # return f"Added Student {userid} Successfully"
        except Exception as e:
            print(str(e)), 500
        except NotUniqueError as e:
            print(str(e))
            return {"msg":"some required fields already exists in db"},403

    #update user data
    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(put_user)
    def put(self):
        try:
            body = request.get_json()
            # print(body)
            if body is not None:
                check = check_userid(body["userid"],"put")
                if check == True:
                    index,data = data_indexing(body)
                    datalist = make_a_list(index,data)
                    # print(datalist)

                    user = Models.User(datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6],datalist[7],datalist[8])
                    response = user.update_user()

                    print(response)
                   
                    if response == 200:
                        return {"message":response},200
                    else:
                        return {"message":response},406
                   
                else:
                    return {
                        "message" : "Enter Userid" 
                    },400
            else:
                return{"message":"Enter Attributes"},400
        except Exception as e:
            print(str(e)), 500

    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(delete_user)
    def delete(self):
        try:
            body = request.get_json()
            print(body["userid"])
            check = check_userid(body["userid"],"delete")
            print(check)
            if check[-1] == 200:
                data = Models.User(body["userid"])
                response = data.delete_user()
                if response == 200:
                    return {"message":f"User {body['userid']} Deleted Successfully"},200
                else:
                    return {"message":response}
            else:
                return{"message":check}
        except Error as e:
            print(str(e))

            return{"message":e}

class Download(Resource):
    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    def get(self):
        pass


        

namespace.add_resource(User,'/dashboard')
namespace.add_resource(Download,'/download')


