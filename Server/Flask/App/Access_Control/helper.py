from App import Models
from datetime import datetime,timezone
from dateutil import tz

def check_userid(value,flag):
    user = Models.User(userid= value)
    _,status = user.getAUser() 

    if flag == "get":
        if status ==200: 
            return 200
        else:
            return False

    if flag == "delete":
        if status ==200: 
            return 200
        else:
            return False

    if flag == "put":
        if status == 200:
            userid = [int(x) for x in str(value)]
            if len(userid) == 10:
                return True
            else:
                return False

    if flag == "post":
        userid = [int(x) for x in str(value)]
        data = [2,2,2]
        if userid[:3] == data:
            return True
        else:
            return False

    if flag == "login":
        if status == 200:
            return True
        else:
            return False

def check_roomno(value,flag):

    roomno = Models.Rooms(value)
    _,status = roomno.getRoom()

    if flag == "get":
        if status == 200:
            return 200
        else:
            return False

    if flag == "post":

        if status == 404: 
            return 200
        else:
            return "Room Already Exists"

    if flag == "delete":

        if status != 404: 
            return 200
        else:
            return "Room Does Not Exists"

def check_update_user(value,flag):

    user = Models.Access_Control(userid=value)
    _,status = user.getAACData(flag)

    if flag == "userid":
        if status == 200:
            return 200
        else:
            return False

    if flag == "profid":
        if status == 200:
            return 200
        else:
            return False
    
def  check_access_roomno(value,reqflag,paramflag):

    roomno = Models.Access_Control(rid=value)
    _,status = roomno.getAACData(paramflag)

    if reqflag == "put":
        if status == 200: 
            return 200
        else:
            return 404

def check_time(timein,timeout,userid,role):

    dbtimein = Models.Logs().getALog("timein",userid,role)
    dbtimeout = Models.Logs().getALog("timeout",userid,role)

    if timein != "":

        if dbtimein == None:
            return "New"
        elif dbtimein != "":
            print("inside the elif")

            # time from API
            striptimein = datetime.strptime(timein,'%Y-%m-%d %H:%M:%S')
            print(striptimein)

            # time from DB
            stripdbtime = datetime.strptime(dbtimein,'%Y-%m-%d %H:%M:%S')
            print(stripdbtime)

            # calculating time difference between API time and DB time 
            total_time = (striptimein - stripdbtime)
            total_time_mins = total_time.total_seconds()/60
            print(total_time_mins)

            if total_time_mins >= 10:
                return "replace"
            else:
                return "dump"
        elif dbtimeout != "":
            pass

        else:

            return False


    elif timeout != "":

        if dbtimeout == "":
            return "New"
        elif dbtimeout != "":

            # time from API
            striptimeout = datetime.strptime(timeout,'%Y-%m-%d %H:%M:%S')
            print(striptimeout)

            # time from DB
            stripdbtimeout = datetime.strptime(dbtimeout,'%Y-%m-%d %H:%M:%S')
            print(stripdbtimeout)

            # calculating time difference between API time and DB time 
            total_time = (striptimeout - stripdbtimeout)
            total_time_mins = total_time.total_seconds()/60
            print(total_time_mins)
            
            if total_time_mins >= 10:
                return "replace"
            else:
                return "dump"

        else:

            return False

def check_role(value):

    u = Models.User(userid=value)
    status = u.getAUser("role")

    if status == 1:
        return 1
    else:
        return 0

def check_secrets(value):
    SECRETS=["62E3AC722D002BE1"]
    rdata = ""
    for i in SECRETS:
        if i == value:
            rdata = "valid"
            break
        else:
            rdata = "invalid" 
            
    return rdata

def add_duration(userid,status,timeout):

    if status == 200:
    
        status = check_role(userid)
        dbDuration = Models.Logs().getALog("duration",userid,status)

        if dbDuration == "None":
            pass
            dbtimein = Models.Logs().getALog("timein",userid) 

            # time from DB
            stripdbtime = datetime.strptime(dbtimein,'%Y-%m-%d %H:%M:%S')
            print(stripdbtime)

            striptimeout = datetime.strptime(timeout,'%Y-%m-%d %H:%M:%S')
            print(striptimeout)

        else:

            dbtimeout = Models.Logs().getALog("timeout",userid)

            # timeout from API
            striptimeout = datetime.strptime(timeout,'%Y-%m-%d %H:%M:%S')
            print(striptimeout)

            # time from DB
            stripdbtimeout = datetime.strptime(dbtimeout,'%Y-%m-%d %H:%M:%S')
            print(stripdbtimeout)

            total_time = (striptimeout - stripdbtimeout)
            total_time_mins = total_time.total_seconds()/60
            print(total_time_mins)

            total_duration = (total_time_mins + dbDuration)

