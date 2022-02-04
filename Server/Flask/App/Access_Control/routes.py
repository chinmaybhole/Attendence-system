from sqlite3.dbapi2 import Error
from flask import request
from App import Models, api
from flask_restx import Resource,Namespace
from App.Access_Control.serializer import *
from App.Access_Control.helper import *

namespace = Namespace("Access","Insert Update of Access Control Data")

class Access_control(Resource):

    @api.expect(access_model)
    def post(self):
        try:
            body = request.get_json()
            print(body)
            if body is not None:
                if body["userid"] == 0:
                    userid = None
                    check = check_userid(body["userid"],"post")
                    if check == True:
                        ac = Models.Access_Control(body["rid"],userid,body["profid"])
                        log = Models.Logs(timein=body["timein"],timeout=body["timeout"])
                        acdata = ac.insert_access_control()
                    else:
                        return {"Warning":"userid Not Found"}
                elif body["profid"] == 0:
                    profid = None
                    check = check_userid(body["userid"],"post")
                    if check == True:
                        ac = Models.Access_Control(body["rid"],body["userid"],profid)
                        log = Models.Logs(timein=body["timein"],timeout=body["timeout"])
                        acdata = ac.insert_access_control()
                    else:
                        return {"Warning":"profid Not Found"}
                else:
                    return{"Warning":"Values userid and profid cannot be null"}
            else:
                return {"Error":"Parameters Cannot be Null"},404
        except Error as e:
            print(str(e))
            return e

    @api.expect(access_model)
    def put(self):
        try:
            body = request.get_json()
            if body is not None:
                if body["secrets"] != "":
                    checkSecret = check_secrets(body["secrets"])
                    if checkSecret == "valid":
                        if body["rid"] is not None:
                            checkrommno = check_access_roomno(body["rid"],"put","rid")
                            if checkrommno == 200:
                                check = check_userid(body["userid"],"put")
                                role = check_role(body["userid"])
                                if check == True and role == 0: #Professor
                                    userid = None
                                    userid_exists = check_update_user(body["userid"],"profid")
                                    if userid_exists == 200:
                                        checkTime = check_time(body["timein"],body["timeout"],body["userid"])
                                        if checkTime == "New":
                                            ac = Models.Access_Control(body["rid"],userid,body["userid"])
                                            log = Models.Logs(timein=body["timein"],timeout=body["timeout"])
                                            # acdata = ac.insert_access_control()
                                        elif checkTime == "":
                                            pass
                                    else:
                                        return {"Error":"Profid Not Found"},404
                                elif check == True and role == 1: #Student
                                    profid = None 
                                    userid_exists = check_update_user(body["userid"],"userid")
                                    print(userid_exists)
                                    if userid_exists == 200:
                                        checkTime = check_time(body["timein"],body["timeout"],body["userid"])
                                        print(checkTime)
                                        if checkTime == "New":
                                            ac = Models.Access_Control(body["rid"],body["userid"],profid)
                                            log = Models.Logs(timein=body["timein"],timeout=body["timeout"])
                                            # acdata = ac.insert_access_control()
                                        elif checkTime == "":
                                            pass
                                    else:
                                        return {"Error":"Userid Not Found"},404
                                elif check == False:
                                    return {"Error":"Invalid Userid"},404
                                else:
                                    return{"Error":"userid Cannot be Null"},406    
                            else:
                                return {"Error": checkrommno},404
                        else:
                            return {"Error": "Room Id Cannot be Empty"},406
                    else:
                        return {"Error":"Secret is Invalid"},404
                else:
                    return{"Error": "Secret Cannot be Null"},406
            else:
                return {"Error":"Parameters Cannot be None"},406

        except Error as e :
            print(str(e))
            return{"Error":e}

namespace.add_resource(Access_control,"/access")