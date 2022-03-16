from App import Models
from datetime import datetime,timedelta
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

def check_update_user(userid,rid,flag):

    user = Models.Access_Control(userid=userid,rid= rid)
    _,flagstatus = user.getAACData(flag)
    _,roomstatus = user.getAACData("rid")

    if flag == "userid":
        if flagstatus == 200 and roomstatus == 200:
            return 200
        else:
            return False

    if flag == "profid":
        if flagstatus == 200 and roomstatus == 200:
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
    print("DB timeout:",dbtimeout)
    print("API timeout:",timeout)


    if timein != "":

        if dbtimein == None:
            return "New"
        elif dbtimein != "":
            print("inside the elif")

            # time from API
            striptimein = datetime.strptime(timein,'%Y-%m-%d %H:%M:%S')

            # time from DB
            stripdbtime = datetime.strptime(dbtimein,'%Y-%m-%d %H:%M:%S')

            # calculating time difference between API time and DB time 
            total_time = (striptimein - stripdbtime)
            total_time_mins = total_time.total_seconds()/60

            if total_time_mins >= 10:
                return "replace"
            else:
                return "dump"
        elif dbtimeout != "":
            pass

        else:

            return False


    elif timeout != "":

        if dbtimeout == None:
            return "New"
        elif dbtimeout != "":
            print("inside elif")


            # time from API
            striptimeout = datetime.strptime(timeout,'%Y-%m-%d %H:%M:%S')

            # time from DB
            stripdbtimeout = datetime.strptime(dbtimeout,'%Y-%m-%d %H:%M:%S')

            # calculating time difference between API time and DB time 
            total_time = (striptimeout - stripdbtimeout)
            total_time_mins = total_time.total_seconds()/60
            
            if total_time_mins >= 10:
                return "replace"
            else:
                return "dump"

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

def add_duration(userid,timeout,role):
    """
    Add the duration of the user to the database.
    @param userid - the userid of the user to add the duration to.
    @param timeout - the timeout of the user.
    """
    print("inside add duration")
    status = check_role(userid)
    dbDuration = Models.Logs().getALog("duration",userid,status) 
    print(dbDuration)
    print("status:",status)
    if status == 1: #student
    
        if dbDuration == None: 
            dbtimein = Models.Logs().getALog("timein",userid,status)
            db_timein = dbtimein.split(" ",1)
            dbtimein = db_timein[1]

            # time from DB
            # stripdbtimein = datetime.strptime(dbtimein,'%Y-%m-%d %H:%M:%S')
            stripdbtimein = datetime.strptime(dbtimein,'%H:%M:%S')
            # floattimein = stripdbtimein.timestamp()

            # timeout from API
            time_out = timeout.split(" ",1)
            timeout = time_out[1]

            # striptimeout = datetime.strptime(timeout,'%Y-%m-%d %H:%M:%S')
            striptimeout = datetime.strptime(timeout,'%H:%M:%S')
            # floatdbtimeout = striptimeout.timestamp()

            total_time = (striptimeout - stripdbtimein)
            print(total_time)

            # total_duration = (total_time + floatdbtimeout)
            # print("total mins: ",total_duration)

            # conversion = timedelta(seconds=total_duration)
            time_convert = str(total_time)

            log_message,logstatus = Models.Logs(duration=time_convert).add_log_duration(role=role,userid=userid)
            return logstatus

        else:
            # timeout from API
            time_out = timeout.split(" ",1)
            timeout = time_out[1]
            striptimeout = datetime.strptime(timeout,'%H:%M:%S')
            onlytimeout = striptimeout - datetime(1900, 1, 1)
            print("API timeout: ",onlytimeout)

            # timein from temp DB
            temptime,status = Models.TempTable(userid=userid).get_temp_data()
            temp_timein = temptime.split(" ",1)
            temptimein = temp_timein[1]

            striptemptimein = datetime.strptime(temptimein,'%H:%M:%S')
            onlytemptimein = striptemptimein - datetime(1900,1,1)
            print("DB timein: ",onlytemptimein)

            total_secs = (onlytimeout - onlytemptimein)
            print("total secs: ",total_secs)

            # Adding Log duration and new time difference of api timeout and temp table timeout 
            stripduration = datetime.strptime(dbDuration,"%H:%M:%S")
            onlytime = stripduration - datetime(1900, 1, 1)

            total_duration = (total_secs + onlytime)
            print("total_duration:",total_duration)
            time_convert = str(total_duration)

            logstatus,status = Models.Logs(duration=time_convert).add_log_duration(role=role,userid=userid)

            if status == 200:
                Models.TempTable(userid=userid).delete_temp_record()

            return status

    elif status == 0: #professor

        if dbDuration == None: 
            dbtimein = Models.Logs().getALog("timein",userid,status)

            # time from DB
            stripdbtimein = datetime.strptime(dbtimein,'%Y-%m-%d %H:%M:%S')
            floattimein = stripdbtimein.timestamp()

            # timeout from API
            striptimeout = datetime.strptime(timeout,'%Y-%m-%d %H:%M:%S')
            floatdbtimeout = striptimeout.timestamp()

            total_time = (floattimein - floatdbtimeout)
            print(total_time)

            total_duration = (total_time + floatdbtimeout)
            print("total mins: ",total_duration)

            conversion = timedelta(seconds=total_duration)
            time_convert = str(conversion)

            log_message,logstatus = Models.Logs(duration=time_convert).add_log_duration(role=role,userid=userid)
            return logstatus

        else:

            # timeout from API
            time_out = timeout.split(" ",1)
            timeout = time_out[1]
            striptimeout = datetime.strptime(timeout,'%H:%M:%S')
            onlytimeout = striptimeout - datetime(1900, 1, 1)
            print("API timeout: ",onlytimeout)

            # timein from temp DB
            temptime,status = Models.TempTable(userid=userid).get_temp_data()
            temp_timein = temptime.split(" ",1)
            temptimein = temp_timein[1]

            # stripdbtimeout = datetime.strptime(temptimein,'%Y-%m-%d %H:%M:%S')
            striptemptimein = datetime.strptime(temptimein,'%H:%M:%S')
            onlytemptimein = striptemptimein - datetime(1900,1,1)
            print("DB timein: ",onlytemptimein)

            total_secs = (onlytimeout - onlytemptimein)
            print("total secs: ",total_secs)

            # Adding db duration and new time difference of api timeout and db timeout 
            stripduration = datetime.strptime(dbDuration,"%H:%M:%S")
            onlytime = stripduration - datetime(1900, 1, 1)

            total_duration = (total_secs + onlytime)
            print("total_duration:",total_duration)
            time_convert = str(total_duration)

            logstatus,status = Models.Logs(duration=time_convert).add_log_duration(role=role,userid=userid)

            if status == 200:
                Models.TempTable(userid=userid).delete_temp_record()

            return status


