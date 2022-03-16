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
                        log = Models.Logs(timein=body["timein"])
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
                            checkroom = check_roomno(body["rid"],"get")
                            if checkroom == 200:
                                checkaccessrommno = check_access_roomno(body["rid"],"put","rid")
                                userid_exists = check_update_user(body["userid"],body["rid"],"userid")
                                profid_exists = check_update_user(body["userid"],body["rid"],"profid")

                                print(checkaccessrommno,userid_exists,profid_exists)

                                if checkaccessrommno == 200 and (userid_exists == 200 or profid_exists == 200):
                                    check = check_userid(body["userid"],"put")
                                    role = check_role(body["userid"])
                                    if check == True and role == 0: #Professor
                                        userid = None
                                        if profid_exists == 200:
                                            if body["timein"] != "" and body["timeout"] != "":

                                                return {"Error": "Both Timein and Timeout cannot be entered at the same time"},406

                                            elif body["timein"] == "" and body["timeout"] == "":

                                                return {"Error": "Both Timein and Timeout cannot be Null at the same time"},406
                                                
                                            else:
                                                checkTime = check_time(body["timein"],body["timeout"],body["userid"],role)
                                                print("checktime",checkTime)
                                                if checkTime == "New": # new data to insert

                                                    log = Models.Logs(timeout=body["timeout"])
                                                    duration_status = add_duration(body["userid"],body["timeout"],role)
                                                    if duration_status == 200:
                                                        logdata,status = log.update_log(body["userid"],role)
                                                        if status == 200:
                                                            return {"message":logdata},status
                                            
                                                elif checkTime == "replace": # to add the current data to temp table
                                                    
                                                    if body["timein"] != "":
                                                        temp = Models.TempTable(userid=body["userid"],timein=body["timein"])
                                                        temp.create_temp()
                                                        status = temp.insert_temp()

                                                        return {"message":status}

                                                    elif body["timeout"] != "":
                                                        log = Models.Logs(timeout=body["timeout"])
                                                        duration_status = add_duration(body["userid"],body["timeout"],role)

                                                        if duration_status == 200:
                                                            logdata,status = log.update_log(body["userid"],role)
                                                            if status == 200:
                                                                return {"message":logdata},status


                                                elif checkTime == "dump": # to dump the current data

                                                    return {"message":"Data Dumped due to Non Matching Properties"},200

                                        else:
                                            return {"Error":"Profid Not Found"},404
                                    elif check == True and role == 1: #Student
                                        profid = None 
                                        
                                        if userid_exists == 200:
                                            if body["timein"] != "" and body["timeout"] != "":

                                                return {"Error": "Both Timein and Timeout cannot be entered at the same time"},406

                                            elif body["timein"] == "" and body["timeout"] == "":

                                                return {"Error": "Both Timein and Timeout cannot be Null at the same time"},406
                                                
                                            else:
                                                checkTime = check_time(body["timein"],body["timeout"],body["userid"],role)

                                                if checkTime == "New": # update data to insert

                                                    log = Models.Logs(timeout=body["timeout"])
                                                    duration_status = add_duration(body["userid"],body["timeout"],role)
                                                    if duration_status == 200:
                                                        logdata,status = log.update_log(body["userid"],role)
                                                        if status == 200:
                                                            return {"message":logdata},status
                            
                                                if checkTime == "replace": # to replace the current data with old
                                                    if body["timein"] != "":
                                                        temp = Models.TempTable(userid=body["userid"],timein=body["timein"])
                                                        temp.create_temp()
                                                        tempdata,status = temp.insert_temp()

                                                        return {"message":tempdata},status
        
                                                    elif body["timeout"] != "":
                                                        log = Models.Logs(timeout=body["timeout"])
                                                        duration_status = add_duration(body["userid"],body["timeout"],role)

                                                        if duration_status == 200:
                                                            logdata,status = log.update_log(body["userid"],role)
                                                            if status == 200:
                                                                return {"message":logdata},status

                                                elif checkTime == "dump": # to dump the current data

                                                    return {"message":"Data Dumped due to Non Matching Properties"},200

                                        else:
                                            return {"Error":"Userid Not Found"},404
                                    elif check == False:
                                        return {"Error":"Invalid Userid"},404
                                    else:
                                        return{"Error":"userid Cannot be Null"},406    
                                else:
                                    check = check_userid(body["userid"],"put")
                                    role = check_role(body["userid"])
                                    if check == True and role == 0: # Professor
                                        if body["timein"] != "" and body["timeout"] != "":
                                            return {"Error": "Both Timein and Timeout cannot be entered at the same time"},406

                                        elif body["timein"] == "" and body["timeout"] == "":
                                            return {"Error": "Both Timein and Timeout cannot be Null at the same time"},406
                                            
                                        else:
                                            userid = None
                                            checkTime = check_time(body["timein"],body["timeout"],body["userid"],role)
                                            print("checktime: ",checkTime)
                                            if checkTime == "New": # new data to insert
                                                getuser = Models.User(userid=body["userid"])
                                                user = getuser.getAUser("insertaccess")
                                                ac = Models.Access_Control(body["rid"],userid,getuser)
                                                acdata,status = ac.insert_access_control()

                                                if status == 200:
                                                    getac = Models.Access_Control().getAllACData("insertlog")

                                                    log = Models.Logs(access_srno=getac,timein=body["timein"])
                                                    logdata = log.insertDataToLog()

                                                return {"message": acdata},status

                                    elif check == True and role == 1: #Student
                                        if body["timein"] != "" and body["timeout"] != "":
                                            return {"Error": "Both Timein and Timeout cannot be entered at the same time"},406

                                        elif body["timein"] == "" and body["timeout"] == "":
                                            return {"Error": "Both Timein and Timeout cannot be Null at the same time"},406
                                            
                                        else:
                                            profid = None
                                            checkTime = check_time(body["timein"],body["timeout"],body["userid"],role)
                                            print("checktime: ",checkTime)
                                            if checkTime == "New": # new data to insert
                                                print(body["userid"])
                                                getuser = Models.User(userid=body["userid"]).getAUser("insertaccess")
                                                ac = Models.Access_Control(body["rid"],getuser,profid)
                                                acdata,status = ac.insert_access_control()

                                                if status == 200:
                                                    getac = Models.Access_Control().getAllACData("insertlog")
                                                    print("access data",getac)

                                                    log = Models.Logs(access_srno=getac,timein=body["timein"])
                                                    logdata,status = log.insertDataToLog()

                                                    print("log status",status)

                                                    if status == 200:
                                                        return {"message": acdata}
                                                    else:
                                                        return {"Error":"An Error Occored"}
                                    else:
                                        return {"message":"User Role Not Found"},404
                            else:
                                return {"Error": "Room Entered Does Not Exits"},404
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