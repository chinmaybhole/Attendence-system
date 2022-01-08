from flask import Blueprint,request
from App import Models, api
from flask_restx import Resource,reqparse,Namespace
from App.Admin.seralizer import *
from Flask.passw import hash_passwd

users = Models.User()
rooms = Models.Rooms()
ac = Models.Access_Control()


# routes = Blueprint("routes",__name__)

namespace = Namespace('Admin', description= "All About Admin API's")



class Users(Resource):
    def create_user(self):
        pass
    def update_user(self):
        pass
    def detele_user(self):
        pass

class Dashboard(Resource):
    # get all data
    def get(self):
        try:
            u=users.getAllUsers()
            a= ac.getAllACData()
            r= rooms.getAllRooms()
            
            return {'User':u,"Access_Control":a,"Rooms":r}
            
        except Exception as e:
            print(str(e))


class GetAUser(Resource):   
    # get a User
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
            user = request.args.get('userid')
            print(user)
            u = users.getAUser(user)
            print(u)
            return {"user":u},200
        except Exception as e:
            print(str(e)),500

        return ""

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
    def post(self):
        try:
            userid = request.form['userid'],
            fname = request.form['fname'],
            lname = request.form['lname'],
            passw = request.form['passw'],
            rollno = request.form['rollno'],
            div = request.form['div'],
            dept = request.form['dept'],
            phone = request.form['phone'],
            isstudent = request.form['isStudent'] 
            passw = hash_passwd(passw) # hashing the raw password

            data =[userid,fname,lname,passw,rollno,div,dept,phone,isstudent]

            users.insert_user(data)

            print(type(userid))
            print(type(fname))




            return f"Added Student {userid} Successfully"
        except Exception as e:
            print(str(e)), 500

namespace.add_resource(Dashboard,'/dashboard')
namespace.add_resource(Download,'/download')
namespace.add_resource(Users,'/users')
namespace.add_resource(GetAUser,'/getauser')


