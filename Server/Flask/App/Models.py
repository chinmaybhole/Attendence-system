import sqlite3
from sqlite3.dbapi2 import Error

conn = sqlite3.connect('test.sqlite',check_same_thread=False)
conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


#################################################### USERS MODEL ##########################################################

class User:

    def __init__(self, userid=None, fname=None, lname=None, passw=None, rollno=None, div=None,dept=None, phone=None, isStudent=None, isAdmin=None,srno=None):
        self.srno = srno
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.passw = passw
        self.rollno = rollno
        self.div = div
        self.dept = dept
        self.phone = phone
        self.isStudent = isStudent
        self.isAdmin = isAdmin

    # create user table
    def create_user():
        c.execute('''CREATE TABLE USERS
                (
                    srno INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    userid INTEGER,
                    fname TEXT NOT NULL,
                    lname TEXT NOT NULL,
                    passw TEXT NOT NULL,
                    rollno INTEGER,
                    div INTEGER,
                    dept TEXT NOT NULL,
                    phone INTEGER NOT NULL,
                    isStudent INTEGER NOT NULL,
                    isAdmin INTEGER NOT NULL
                ); ''')
        conn.commit()
            
    # insert user to table
    def insert_user(self):
        #TODOChinmay : To unpack data and plot it to insert command and to return the after process for eg (success, failed)
        try:
            c.execute("INSERT INTO USERS(userid,fname,lname,passw,rollno,div,dept,phone,isStudent) VALUES(:userid,:fname,:lname,:passw,:rollno,:div,:dept,:phone,:isStudent)",{'userid': self.userid,'fname': self.fname,'lname': self.lname,'passw':self.passw,'rollno': self.rollno,'div':self.div,'dept':self.dept,'phone': self.phone,'isStudent': self.isStudent})
            conn.commit()

            return f"User {self.userid} added Successfully",200
        except Error as e :
            print(str(e))

            return e

    # Delete Data of table user
    def delete_user(self):
        try:
            c.execute("DELETE from USERS WHERE userid = :userid",{'userid': self.userid})
            conn.commit()

            return {f"User {self.userid} has been deleted"},200
        except Error as e:
            print(str(e))

            return {"message":e},406

    # Update Data of table user
    def update_user(self):
        try:
            fields_to_set = []
            field_values = []
            # print(self)
            for attri in vars(self):

                data = getattr(self,attri)
              
                if data is not None:
                    
                    fields_to_set.append(attri +"= "+ "?")
                    field_values.append(getattr(self,attri))
           
            fields_to_set.pop(0)
            field_values.pop(0)       
            set_statement = ", ".join(fields_to_set)
            field_values.append(self.userid)

            c.execute(" UPDATE USERS SET "+set_statement+" WHERE userid = ?",field_values)
            conn.commit()

            return f"user {self.userid} has been updated",200
        except Error as e:
            print(str(e))

            return {"message":e},406

    # get all users
    def getAllUsers(self,role=None):
        field_value = ""

        if role == "Admin":
            values = ["srno","userid","fname","lname","passw","rollno","div","dept","phone","isStudent"]
            
        else:
            values = "*"    

        field_value = ",".join(values)    
        print(field_value)
        sqldata = c.execute(" SELECT "+field_value+" FROM USERS ")
        dictdata = [dict(ix) for ix in sqldata]

        return dictdata
    
    # get a single user
    def getAUser(self,flag=None):
        sqldata = c.execute("SELECT srno,userid,fname,lname,rollno,passw,div,dept,phone FROM USERS WHERE userid = :userid",{'userid':self.userid})
        dictdata = [dict(ix) for ix in sqldata]
                
        if flag == "login":
            data = dictdata[0]["passw"]
            return data

        if flag == "role":
            sqldata = c.execute("SELECT isStudent FROM USERS WHERE userid = :userid",{'userid':self.userid})
            dictdata = [dict(ix) for ix in sqldata]  
            data = dictdata[0]["isStudent"]

            return data

        if flag == "insertaccess":
            sqldata = c.execute("SELECT srno FROM USERS WHERE userid = :userid",{'userid':self.userid})
            dictdata = [dict(ix) for ix in sqldata] 
            print(self.userid) 
            data = dictdata[0]["srno"]

            return data


        if sqldata is None or len(dictdata) == 0:
            print("No User data")
            return "No User Found",404
        else:
            return dictdata,200

    # get all students
    def getStudent():
        c.execute(" SELECT * FROM USERS WHERE isStudent = 1")
        print(c.fetchall())

    # get all professors
    def getProfessor(conn,c):
       profid =  c.execute(" SELECT * FROM USERS WHERE isStudent = 0")

        # pprint(c.fetchall())

    def __repr__(self):
        return f"Users('{self.srno}','{self.userid}','{self.fname}','{self.lname}','{self.passw}','{self.rollno}','{self.div}','{self.dept}','{self.phone}','{self.isStudent}','{self.isAdmin}')"

#################################################### ROOMS MODEL ##########################################################

class Rooms:

    def __init__(self, roomno=None, roomname=None):
        self.roomno = roomno
        self.roomname = roomname
       
    # create rooms
    def create_rooms():
           
            c.execute("""CREATE TABLE ROOMS
                        (
                            rid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            roomno INTEGER NOT NULL, 
                            roomname TEXT NOT NULL,
                        );
                    """)
            conn.commit()

    # Insert Data Into table rooms
    def insert_rooms(self):
        try:
            c.execute("INSERT INTO ROOMS(roomno,roomname) VALUES(:roomno,:roomname);",{'roomno': self.roomno,'roomname':self.roomname})
            conn.commit()

            return f"Room {self.roomno} is been Added"
        except Error as e:
            print(str(e))

            return{"Error":e}
    
    # Delete Data from table rooms
    def delete_rooms(self):
        try:
            c.execute("DELETE FROM ROOMS WHERE roomno = :roomno",{'roomno': self.roomno})
            conn.commit()

            return {"message":f"Room {self.roomno} is been deleted"}
        except Error as e:
            print(str(e))

            return{"Error":e}

    # Update Data Into table rooms
    def update_rooms_no(self):
        try:
            c.execute("UPDATE ROOMS SET roomno = :roomno WHERE roomname = :roomname",{'roomno':self.roomno,'roomname':self.roomname})
            conn.commit()
        except Error as e:
            print(str(e))

            return{"Error":e}

    # get all rooms
    def getAllRooms(self):
        try:
            sqldata = c.execute("SELECT * FROM ROOMS")
            dictdata = [dict(ix) for ix in sqldata]

            return dictdata
        except Error as e:
            print(str(e))

            return{"Error":e}

    # get one room
    def getRoom(self):
        try:
            sqldata = c.execute(" SELECT * FROM ROOMS WHERE roomno = :roomno", {'roomno':self.roomno})
            dictdata = [dict(ix) for ix in sqldata]

            if sqldata is None or len(dictdata) == 0:
                print("No Room data")
                return "No Room Found",404
            else:
                return dictdata,200
        except Error as e:
            print(str(e))

            return{"Error": e}

    def __repr__(self):
        return f"Room('{self.roomno}','{self.roomname}')"

#################################################### ACCESS-CONTROL MODEL #################################################

class Access_Control:

    def __init__(self,rid=None,userid=None,profid=None,srno=None):
        self.srno = srno
        self.userid = userid
        self.rid = rid
        self.profid = profid

    # create access_control
    def create_access_control(self):
        c.execute("""CREATE TABLE ACCESS_CONTROL
                    (
                        srno INTEGER PRIMARY KEY AUTOINCREMENT,
                        userid INTEGER,
                        rid INTEGER NOT NULL,
                        profid INTEGER,
                        FOREIGN KEY(userid) REFERENCES USERS(srno),
                        FOREIGN KEY(profid) REFERENCES USERS(srno),
                        FOREIGN KEY(rid) REFERENCES ROOMS(roomno)
                    );
                """)
        conn.commit()

    # def access_cont(conn,c):
    #     with conn:
    #         li = c.execute('SELECT userid,isStudent FROM users')
    #         li = c.fetchall()
    #         for i,k in li:
    #             userid = None
    #             profid = i
    #             if k == 1:
    #                 userid = i
    #                 profid = None
    #             c.execute("""INSERT INTO ACCESS_CONTROl(userid,rid,profid) VALUES(:userid,:rid,:profid)""",{'userid':userid,'rid': 801,'profid':profid})
    #             conn.commit()
    #     return None
    #insert data to table access_system
    def insert_access_control(self):
        try:
            fields_to_set = []
            values_to_set = []
            field_values = []

            for attri in vars(self):
                data = getattr(self,attri)
                if data is not None:
                    print(attri,data)
                    fields_to_set.append(attri)
                    values_to_set.append("?")
                    field_values.append(getattr(self,attri))
                
            set_statement = ", ".join(fields_to_set)
            set_values= ",".join(values_to_set)
            
            # print(field_values,fields_to_set,values_to_set)
            print(set_statement)
            print(set_values)
            print(field_values)


            c.execute("INSERT INTO ACCESS_CONTROL("+set_statement+") VALUES("+set_values+")",field_values)
            conn.commit()

            return f"Data of user {self.userid} is Added",200

        except Error as e:
            print(str(e))
            return e
            # c.execute("INSERT INTO ACCESS_CONTROL(userid,roomid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout)",{'userid':ac.userid,'roomid':ac.roomid,'timein': ac.timein,'timeout': ac.timeout})

    def getAACData(self,paramflag):
        try:

            if paramflag == "rid":
                sqlrmdata = c.execute("SELECT rid FROM ACCESS_CONTROL WHERE "+paramflag+"= :rid",{"rid":self.rid})
                rmdatadict = [dict(ix) for ix in sqlrmdata]

                if sqlrmdata is None or len(rmdatadict) == 0:
                    print("No Rooms Found Access Control data")
                    return "No Rooms Found",404
                else:
                    return rmdatadict,200

            else:
                sqldata = c.execute("SELECT * FROM ACCESS_CONTROL WHERE "+paramflag+"= (SELECT srno FROM USERS WHERE userid = :srno)",{"srno":self.userid})
                datadict = [dict(ix) for ix in sqldata]

                if sqldata is None or len(datadict) == 0:
                    print("No User Found in Access Control data")
                    return "No User Found",404
                else:
                    return datadict,200

        except Error as e :
            print(str(e))
            return e

    # display all data
    def getAllACData(self,flag=None):
        sqldata = c.execute("SELECT * FROM ACCESS_CONTROL")
        dictdata = [dict(ix) for ix in sqldata]

        if flag == "insertlog":
            sqldata = c.execute("SELECT srno FROM ACCESS_CONTROL")
            dictdata = [dict(ix) for ix in sqldata]
            # print("access data",dictdata[-1]["srno"])
            return dictdata[-1]["srno"]

           
        return dictdata

    # update the timeout if timein exists 
    def update_access_data(self):
            c.execute("UPDATE ACCESS_CONTROL SET old.timeout= new.timeout WHERE timein")

#################################################### LOGS MODEL ###########################################################

class Logs:

    def __init__(self,access_srno=None,timein=None,timeout=None,srno=None,duration=None):
        self.srno = srno
        self.access_srno = access_srno
        self.timein = timein
        self.timeout = timeout
        self.duration = duration

    # create logs table
    def create_logs(self):
            c.execute("""CREATE TABLE LOGS (
                        srno INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        timein REAL,
                        timeout REAL,
                        access_srno INTEGER NOT NULL,
                        FOREIGN KEY(access_srno) REFERENCES ACCESS_CONTROL(srno)                            
                    );""")
            
            conn.commit()

            # ("""CREATE TABLE LOGS (
            #             "srno"	INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            #             "timein"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            #             "timeout"	TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            #             "access_srno"	INTEGER NOT NULL,
            #             FOREIGN KEY("access_srno") REFERENCES "ACCESS_CONTROL"("srno")                            
            #         );""")

            # ("""CREATE TABLE LOGS AS 
            #     SELECT USERS.userid AS 'LOGS_uid',
            #     ROOMS.roomno AS 'LOGS_roomno',
            #     ACCESS_CONTROL.timein AS 'LOGS_timein',
            #     ACCESS_CONTROL.timeout AS 'LOGS_timeout'
            #     FROM USERS,ROOMS,ACCESS_CONTROL
            #     WHERE USERS.id = ROOMS.uid
            #     AND ACCESS_CONTROL.timein AND ACCESS_CONTROL.timeout IS NOT NULL;
            #     """)

    # for inserting new data into logs
    def insert_trigger(self):
            c.execute("""CREATE TRIGGER IF NOT EXISTS logs_trigger
                        AFTER INSERT ON ACCESS_CONTROL
                        WHEN new.rid AND new.profid OR new.rid AND new.userid IS NOT NULL
                        BEGIN
                            INSERT INTO LOGS(access_srno,timein,timeout) VALUES(new.srno,new.timein,new.timeout);
                        END;
                    """)
            conn.commit()

    # insert data to logs
    def insertDataToLog(self):
        try:
            print(self.access_srno)
            # print("INSERT INTO LOGS(access_srno,timein) VALUES("+f'{self.access_srno}'+","+f"'{str(self.timein)}'"+")")

            c.execute("INSERT INTO LOGS(access_srno,timein) VALUES("+f'{self.access_srno}'+","+f"'{str(self.timein)}'"+")")
            conn.commit()
            print("rowcount:",c.rowcount)
            if c.rowcount != 0:
                return "Log Inserted Successfully",200
                
        except Error as e:
            print(str(e))
            return e

    # get all logs
    def getAllLogs(self):
        sqldata = c.execute("SELECT * FROM LOGS")
        dictdata = [dict(ix) for ix in sqldata]
        
        return dictdata
    
    def getALog(self,paramflag,userid,status=None):
        try:
                if status == 1:
                    sqluserdata = c.execute("SELECT srno FROM ACCESS_CONTROL WHERE userid = (SELECT srno FROM USERS WHERE userid = "+str(userid)+")")
                    userdict = [dict(ix) for ix in sqluserdata]
                    # print("access data",userdict)
                    
                    if len(userdict) == 0:
                        print("no data in access")
                        return None
                    else:
                        acdata = userdict[-1]["srno"] #getting the latest log of Student

                        sqldata = c.execute("SELECT "+paramflag+" FROM LOGS WHERE access_srno = "+str(acdata))
                        dictdata = [dict(ix) for ix in sqldata]
                        print(len(dictdata))

                        if sqldata == None or len(dictdata) == []:
                            print("no data in log")
                            return None
                        else:
                            print("log data",dictdata)
                            data = dictdata[0][paramflag]

                            return data

                elif status == 0:
                    sqluserdata = c.execute("SELECT srno FROM ACCESS_CONTROL WHERE profid = (SELECT srno FROM USERS WHERE userid = "+str(userid)+")")
                    userdict = [dict(ix) for ix in sqluserdata]

                    if sqluserdata is None or len(userdict) == 0:
                        return None
                    else:
                        acdata = userdict[-1]["srno"] #getting the latest log of Professor

                        sqldata = c.execute("SELECT "+paramflag+" FROM LOGS WHERE access_srno = "+str(acdata))
                        dictdata = [dict(ix) for ix in sqldata]
                        if sqluserdata is None or len(userdict) == 0:
                            return None
                        else:
                            data = dictdata[0][paramflag]

                            return data

        except Error as e:
            print(str(e))

            return e

    def update_log(self,userid,role):
        try:
            fields_to_set = []
            values_to_set = []
            print(userid)

            for attri in vars(self):
                data = getattr(self,attri)
                if data is not None:
                    print(attri,data)
                    fields_to_set.append(attri+"= ")
                    values_to_set.append(getattr(self,attri))
                    # field_values.append(getattr(self,attri))
                
            set_statement = ", ".join(fields_to_set)
            set_values= ",".join(values_to_set)
            
            print(set_statement+f"'{set_values}'")

            if role == 1:
           
                sqluserdata = c.execute("SELECT srno FROM ACCESS_CONTROL WHERE userid = (SELECT srno FROM USERS WHERE userid = "+str(userid)+")")
                userdict = [dict(ix) for ix in sqluserdata]

                acdata = userdict[-1]["srno"] #getting the latest log of Student

            elif role == 0:
                sqluserdata = c.execute("SELECT srno FROM ACCESS_CONTROL WHERE profid = (SELECT srno FROM USERS WHERE userid = "+str(userid)+")")
                userdict = [dict(ix) for ix in sqluserdata]

                acdata = userdict[-1]["srno"] #getting the latest log of Student

            c.execute("UPDATE LOGS SET "+set_statement+f"'{set_values}' WHERE access_srno = :userid",{"userid":acdata})
            conn.commit()

            return "Data Updated SuccessFully",200

        except Error as e:
            print(str(e))
            return e

    def add_log_duration(self,role,userid):
        try:

            if role == 1:
           
                sqluserdata = c.execute("SELECT srno FROM ACCESS_CONTROL WHERE userid = (SELECT srno FROM USERS WHERE userid = "+str(userid)+")")
                userdict = [dict(ix) for ix in sqluserdata]
                print(userdict)

                acdata = userdict[-1]["srno"] #getting the latest log of Student

                print(acdata)
            elif role == 0:
                sqluserdata = c.execute("SELECT srno FROM ACCESS_CONTROL WHERE profid = (SELECT srno FROM USERS WHERE userid = "+str(userid)+")")
                userdict = [dict(ix) for ix in sqluserdata]
                print(userdict)

                acdata = userdict[-1]["srno"] #getting the latest log of Professor

                print(acdata)

            c.execute("UPDATE LOGS SET duration = :duration WHERE access_srno = :access_srno",{"duration":self.duration,"access_srno":acdata})
            conn.commit()

            return "duration has been updated successfully!",200

        except Error as e:
            print(str(e))

            return e

    def __repr__(self):
        return f"Logs('{self.srno}','{self.access_srno}','{self.timein}','{self.timeout}')"

def download_logs_data():
    try:
        sqldata = c.execute("""
            SELECT 
            LOGS.srno [Srno],
            LOGS.access_srno [Access Id],
            USERS.fname [Name],
            ROOMS.roomno [Roomno],
            LOGS.timein [Timein],
            LOGS.timeout [Timeout],
            LOGS.duration [Duration]
            FROM LOGS
            LEFT JOIN ACCESS_CONTROL ON LOGS.access_srno = ACCESS_CONTROL.srno
            LEFT JOIN USERS ON USERS.fname = (SELECT fname FROM USERS WHERE CASE WHEN ACCESS_CONTROL.userid IS NOT NULL THEN ACCESS_CONTROL.userid = USERS.srno ELSE ACCESS_CONTROL.profid = USERS.srno END)
            LEFT JOIN ROOMS ON ROOMS.roomno = (SELECT roomno FROM ROOMS WHERE ACCESS_CONTROL.rid = ROOMS.roomno)
            """)
        
        dictdata = [dict(ix) for ix in sqldata]

        return dictdata

    except Error as e:
        print(str(e))

        return {"Error": e}

#################################################### TEMP MODEL ###########################################################

class TempTable:
    def __init__(self,userid=None,timein=None):
        self.userid = userid
        self.timein = timein
        
    def create_temp(self):
        try:
            c.execute("""CREATE TEMP TABLE IF NOT EXISTS UserTime
                    (   
                        userid INTEGER PRIMARY KEY,
                        timein TIMESTAMP
                    );""")
            conn.commit()

            if c.rowcount != 0:
                print("temp table:",c.lastrowid)

        except Error as e:
            print(str(e))
            return e
        

    def insert_temp(self):
        try:

            c.execute("INSERT INTO UserTime VALUES(:userid,:timein)",{"userid":self.userid,"timein":self.timein})
            conn.commit()

            if c.rowcount != 0:
                return "Data Registered Successfully",200
        except Error as e:
            print(str(e))
            return e,400

    def get_temp_data(self):
        try:

            # checktemp = c.execute("SELECT name FROM sqlite_temp_master;")
            # print("checktemp:",checktemp)

            sqldata = c.execute("SELECT timein FROM temp.UserTime WHERE userid = :userid",{"userid":self.userid})
            dictdata = [dict(xi) for xi in sqldata]

            if sqldata is None or len(dictdata) == 0:
                return "No Temp Data Found",404
            else:
                data = dictdata[0]["timein"]
                return data,200

        except Error as e:
            print(str(e))
            return e

    def delete_temp_record(self):
        try:
            c.execute("DELETE FROM temp.UserTime WHERE userid = :userid",{"userid":self.userid})
            conn.commit()
        except Error as e :
            print(str(e))

            return e
    
#############################################################################################################################