from sqlite3.dbapi2 import Error
from flask import request
from App import Models, api
from flask_restx import Resource,Namespace
from App.Access_Control.serializer import *
from App.Access_Control.helper import *

namespace = Namespace("Access","Insert Update of Access Control Data")

class Access_control(Resource):

    @api.expect(post_access)
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


namespace.add_resource(Access_control,"/access")