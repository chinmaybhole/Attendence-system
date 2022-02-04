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
    print(status)

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
    
def check_access_roomno(value,reqflag,paramflag):

    roomno = Models.Access_Control(rid=value)
    _,status = roomno.getAACData(paramflag)

    if reqflag == "put":
        if status != 404: 
            return 200
        else:
            return "Room Does Not Exists Can't Update Query"

def check_time(timein,timeout,userid):

    dbtimein = Models.Logs().getALog("timein",userid)
    dbtimeout = Models.Logs().getALog("timeout",userid)

    # u = datetime.utcnow()
    # print(u)
    local_zone = tz.tzlocal()

    


    if dbtimein == "":
        return "New"
    elif dbtimein != "":
        print("inside the elif")

        # time from API
        # rawtime = datetime.fromisoformat(timein).astimezone(local_zone)
        striptime = datetime.strptime(timein,'%Y-%m-%d %H:%M:%S')
        # striptime = datetime.fromisoformat(timein)
        print(striptime.minute)

        # time from DB
        # rawdbtime = datetime.fromisoformat(dbtimein)
        # stripdbtime = datetime.strptime(dbtimein,'%y-%m-%d %H:%M:%S')
        # stripdbtime = datetime.fromisoformat(stripdbtime)

        # print(stripdbtime.minute)

        # total_time = (stripdbtime - striptime)
        # total_secs = total_time.total_seconds()  # calculating time difference between api time and db time
        # print(total_time)

        # if calculated_time >= 10:
        #     return "replace"
        # else:
        #     return "dump"

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
