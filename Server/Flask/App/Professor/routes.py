from sqlite3.dbapi2 import Error
from flask import send_file
from App import Models, api
from flask_restx import Resource,Namespace
from App.Professor.serializer import *
from App.Professor.helper import *
from passw import hash_passwd
import pandas as pd
from io import BytesIO

namespace = Namespace('Professor', description= "All About Professor API's")

class ProfLogin(Resource):
    @api.response(200, "Successful")
    @api.doc(responses=auth_failures)
    @api.expect(prof_login_parser)
    def post(self):
        try:
            body = prof_login_parser.parse_args()
            h_passw = hash_passwd(body["passw"])
            uid_response = check_userid(body["userid"],"login")
            pass_response = check_passw(body["userid"],h_passw,"login")

            if uid_response == 200:
                if pass_response == 200:

                    access_token = create_access_token(body["userid"])

                    refresh_token = create_refresh_token(body["userid"])

                    print("logged In successfully")

                    return{
                        "access_token":access_token,
                        "refresh_token":refresh_token
                    }
                else:
                    print("Invalid Password")
                    return{"message":"Invalid Password"}
            else:
                print("Invalid Userid")
                return{"message":"Invalid Userid"}

        except Error as e:
            print(str(e))
            return{
                "error":e
            }

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

namespace.add_resource(Download,'/download')
namespace.add_resource(ProfLogin,'/login')