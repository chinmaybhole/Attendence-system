import sqlite3
from sqlite3.dbapi2 import Error

conn = sqlite3.connect('test.sqlite',check_same_thread=False)
conn.row_factory = sqlite3.Row # This enables column access by name: row['column_name']
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


#################################################### USERS MODEL #################################################

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


    # user json model
    def user_to_json(self):
        user_dict = {
            'userid': str(self.userid),
            'fname': self.fname,
            'lname':self.lname,
            'dept': self.dept,
            'rollno': self.rollno,
            'div': self.div,
            'phone': self.phone,
        }
        return user_dict

    # create user table
    def create_user():
        c.execute('''CREATE TABLE USERS
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    userid INTEGER NOT NULL,
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
    def getAllUsers(self):
        # field_value = ""
        # data =""
        # print(self.dept)
        # if self.dept is not None:
        #     field_value = "WHERE dept = ?"
        #     data = self.dept
        sqldata = c.execute(" SELECT * FROM USERS ")
        # +field_value,data)
        dictdata = [dict(ix) for ix in sqldata]
        return dictdata
    
    # get a single user
    def getAUser(self,flag=None):
        sqldata = c.execute("SELECT srno,userid,fname,lname,rollno,passw,div,dept,phone FROM USERS WHERE userid = :userid",{'userid':self.userid})
        dictdata = [dict(ix) for ix in sqldata]
                
        if flag == "login":
            data = dictdata[0]["passw"]
            return data

        if sqldata is None or len(dictdata) == 0:
            print("No data")
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

#################################################### ROOMS MODEL #################################################

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
                            uid INTEGER NOT NULL,
                            profid INTEGER NOT NULL,
                            FOREIGN KEY(uid) 
                            REFERENCES USERS(id)
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
                print("No data")
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

    def __init__(self,roomno=None,userid=None,profid=None,srno=None):
        self.srno = srno
        self.userid = userid
        self.roomno = roomno
        self.profid = profid

    # create access_control
    def create_access_control(conn,c):
        with conn:
            c.execute("""CREATE TABLE ACCESS_CONTROL
                        (
                            srno INTEGER PRIMARY KEY AUTOINCREMENT,
                            timein TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            timeout TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            userid INTEGER NOT NULL,
                            rid INTEGER NOT NULL,
                            FOREIGN KEY(userid) REFERENCES USERS(id),
                            FOREIGN KEY(rid) REFERENCES ROOMS(rid)
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
    def insert_access_control(ac,conn,c):
        with conn: 
            c.execute("INSERT INTO ACCESS_CONTROL(userid,profid,rid) VALUES(:userid,:profid,:rid)",{'userid':ac.userid,'profid':ac.profid,'rid':ac.roomno})
            conn.commit()
            # c.execute("INSERT INTO ACCESS_CONTROL(userid,roomid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout)",{'userid':ac.userid,'roomid':ac.roomid,'timein': ac.timein,'timeout': ac.timeout})


    # display all data
    def getAllACData(self):
        sqldata =c.execute("SELECT * FROM ACCESS_CONTROL")
        dictdata = [dict(ix) for ix in sqldata]

        return dictdata

    # update the timeout if timein exists 
    def update_access_data(data,conn,c):
        with conn:
            c.execute("UPDATE ACCESS_CONTROL SET old.timeout= new.timeout WHERE timein")

#################################################### LOGS MODEL #################################################

class Logs:

    def __init__(self,access_srno=None,timein=None,timeout=None,srno=None):
        self.srno = srno
        self.access_srno = access_srno
        self.timein = timein
        self.timeout = timeout

    # create logs table
    def create_logs(conn,c):
        with conn:
            c.executescript("""CREATE TABLE LOGS AS 
                SELECT USERS.userid AS 'LOGS_uid',
                ROOMS.roomno AS 'LOGS_roomno',
                ACCESS_CONTROL.timein AS 'LOGS_timein',
                ACCESS_CONTROL.timeout AS 'LOGS_timeout'
                FROM USERS,ROOMS,ACCESS_CONTROL
                WHERE USERS.id = ROOMS.uid
                AND ACCESS_CONTROL.timein AND ACCESS_CONTROL.timeout IS NOT NULL;
                """)

    # for inserting new data into logs
    def insert_trigger(conn,c):
        with conn:
            c.execute("""CREATE TRIGGER IF NOT EXISTS logs_trigger
                        AFTER INSERT ON ACCESS_CONTROL
                        WHEN new.rid AND new.profid OR new.rid AND new.userid IS NOT NULL
                        BEGIN
                            INSERT INTO LOGS(access_srno) VALUES(new.srno);
                        END;
                    """)

    # insert data to logs
    def insertDataToLog(conn,c,log):
        with conn:
            c.execute(" INSERT INTO LOGS(access_srno) VALUES(:access_srno);",{'access_srno': log.access_srno})

    # get all logs
    def getAllLogs(self):
        sqldata = c.execute("SELECT * FROM LOGS")
        dictdata = [dict(ix) for ix in sqldata]
        
        return dictdata
    


    def __repr__(self):
        return f"Logs('{self.srno}','{self.access_srno}','{self.timein}','{self.timeout}')"

def download_logs_data():
    try:
        sqldata = c.execute("""
            SELECT 
            LOGS.srno [Srno],
            LOGS.timein [Timein],
            LOGS.timeout [Timeout],
            LOGS.access_srno [Access Id],
            USERS.fname [Name],
            ROOMS.roomno [Roomno]
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
#############################################################################################################################