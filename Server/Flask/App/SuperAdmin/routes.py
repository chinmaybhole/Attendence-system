from sqlite3.dbapi2 import Error
from flask import request,send_file
from App import Models, api, token_required
from flask_restx import Resource,Namespace
from App.SuperAdmin.serializer import *
from App.SuperAdmin.helper import *
from passw import hash_passwd
import pandas as pd
from io import BytesIO

namespace = Namespace('SuperAdmin', description= "All About SuperAdmin API's")

class User(Resource):
    # Get User data
    @api.doc(responses={
        200 : "Success",
        406 : "Credentials Not Accecptable", 
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(user_parser)
    @token_required
    def get(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:
                body = request.args
                if "userid" in body:                                                                                                                                                                                                                                      
                    check = check_userid(body["userid"],"get") 
                    if check == 200:
                        usr = Models.User(body["userid"])
                        _,u = usr.getAUser()
                        return {"user":_},200
                    else:
                        return{"Warning": check},404
                else:
                    u= Models.User().getAllUsers()
                    a= Models.Access_Control().getAllACData()
                    r= Models.Rooms().getAllRooms()
                    return {'User':u,"Access_Control":a,"Rooms":r},200
                
            except Exception as e:
                print(str(e))
        else:
            return {"message":"Unauthorized user"},401

    # Post User data
    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(super_post_user)
    @token_required
    def post(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:
                body = request.get_json()
                userid = check_userid(body["userid"],"post")
                phoneno = check_phoneno(body["phone"])
                h_passw = hash_passwd(body["passw"])  # hashing the password
                if userid == True and phoneno == True:
                    if body["rollno"] == 0 and body["div"] == "": # Admin or SuperAdmin
                        rollno = None
                        div = None
                        user = Models.User(body["userid"],body["fname"],body["lname"],h_passw,rollno,div,body["dept"],body["phone"],body["isStudent"],body["isAdmin"],body["isSuperAdmin"])
                        response,status = user.insert_user()

                        return {
                            "message": response
                        },status    

                    else: # Student
                        user = Models.User(body["userid"],body["fname"],body["lname"],h_passw,body["rollno"],body["div"],body["dept"],body["phone"],body["isStudent"])
                        response,status = user.insert_user()

                        return {
                            "message": response
                        },status 
                else:
                    return {"Error":"Userid and Phone no cannot be empty or User Already Exists"},401

            except Exception as e:
                print(str(e)), 500
        else:
            return{"message":"Unauthorized User"},401
            

    # Update User data
    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(super_put_user)
    @token_required
    def put(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:
                body = request.get_json()
                # print(body)
                if body is not None:
                    check = check_userid(body["userid"],"put")
                    if check == True:
                        index,data = data_indexing(body)
                        datalist = make_a_list(index,data)
                        # print(datalist)

                        user = Models.User(datalist[1],datalist[2],datalist[3],datalist[4],datalist[5],datalist[6],datalist[7],datalist[8],None,datalist[10])
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
        else:
            return {"message","Unauthorized User"},401

    # Delete User data
    @api.doc(responses={
        200 : "Success",
        400 : "Bad Request",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(super_delete_user)
    @token_required
    def delete(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
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
        else:
            return {"message","Unauthorized User"},401

class Rooms(Resource):
    @api.doc(responses={
        200 : "Success",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(room_parser)
    @token_required
    def get(self):  
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:  
                room = request.args
                if "roomno" in room:
                    check = check_roomno(room["roomno"],"get") 
                    if check == 200:
                        rms = Models.Rooms(room["roomno"])
                        _,r = rms.getRoom()
                        return {"room":_},200
                    else:
                        return{"message": check},404
                else:
                    r = Models.Rooms().getAllRooms()

                    return{"Rooms": r}
            except Exception as e:
                print(str(e))
        else:
            return {"message":"Unauthorized User"},401
                

    @api.doc(responses={
        200 : "Success",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(super_post_room)
    @token_required
    def post(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:
                body = request.get_json()

                if body is not None:
                    check = check_roomno(body["roomno"],"post")
                    if check == 200:
                        room = Models.Rooms(body["roomno"],body["roomname"])
                        r = room.insert_rooms()

                        return{"message":r}
                    else:
                        return{"message":check}
                else:
                    return{"message": "Values Cannot be Empty"}
            except Exception as e:
                print(str(e))
        else:
            return {"message":"Unauthorized User"},401

    @api.doc(responses={
        200 : "Success",
        406 : "Credentials Not Accecptable",
        404 : "User not found",
        401 : "Token Invalid",
	    403 : "Token is Expired",
        500 : "Internal Server Error"
    })   
    @api.expect(super_delete_room)
    @token_required
    def delete(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:
                body = request.get_json()

                if body is not None:
                    check = check_roomno(body["roomno"],"delete")
                    if check == 200:

                        droom = Models.Rooms(body["roomno"])
                        r = droom.delete_rooms()

                        return {"message": r}
                    else:
                        return {"message":check}
                else:
                    return{"message":"Values Cannot be Empty"}
            except Exception as e:
                print(str(e))
        else:
            return {"message":"Unauthorized User"},401

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
    @token_required
    def get(self):
        t_data = self.get.attrib
        if t_data["isSuperAdmin"] == 1:
            try:

                log = Models.download_logs_data()
                dataset = log

                output = BytesIO()
                pandadata = pd.DataFrame(dataset)
                writer = pd.ExcelWriter(output, engine="xlsxwriter")
                pandadata.to_excel(writer,sheet_name="Sheet1",index=False)
                writer.close()
                output.seek(0)

                return send_file(output,attachment_filename="Attendance_Sheet.xlsx",as_attachment=True)  

            except Error as e:
                print(str(e))

                return{"error":e}     
        else:
            return {"message":"Unauthorized User"},401

namespace.add_resource(User,'/dashboard')
namespace.add_resource(Rooms,'/rooms')
namespace.add_resource(Download,'/download')


