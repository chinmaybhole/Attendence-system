from sqlite3.dbapi2 import Error
from flask import send_file
from App import Models, api, token_required
from flask_restx import Resource,Namespace
from App.Professor.serializer import *
from App.Professor.helper import *
from passw import hash_passwd
import pandas as pd
from io import BytesIO

namespace = Namespace('Professor', description= "All About Professor API's")

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
        if t_data["isStudent"] == 0:
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

namespace.add_resource(Download,'/download')