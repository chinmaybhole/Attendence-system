import datetime
from pprint import pprint 

#################################################### USERS MODEL #################################################

class Users:

    def __init__(self, userid, fname, lname, passw, rollno, dept, phoneno, isStudent,id=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.passw = passw
        self.userid = userid
        self.dept = dept
        self.rollno = rollno
        self.phoneno = phoneno
        self.isStudent = isStudent

    def insert_user(user,conn,c):
        with conn:
            c.execute("INSERT INTO USERS(userid,fname,lname,passw,rollno,dept,phone,isStudent) VALUES(:userid,:fname,:lname,:passw,:rollno,:dept,:phoneno,:isStudent)",{'userid': user.userid,'fname': user.fname,'lname': user.lname,'passw':user.passw,'rollno': user.rollno,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent})

    # Delete Data of table user
    def delete_user(user,conn,c):
        with conn:
            c.execute("DELETE from USERS WHERE userid = :userid",{'userid': user.userid})

    # Update Data of table user
    def update_user(user,conn,c):
        with conn:
            c.execute(""" UPDATE USERS SET fname = :fname AND lname = :lname AND userid = :userid
                    WHERE id = :id""",{':userid':user.userid,'id': user.id, 'fname': user.fname, 'lname': user.lname})

    # get all users
    def getAllUsers(conn,c):
        c.execute(" SELECT * FROM USERS")
        pprint(c.fetchall())

    # get all students
    def getStudent(conn,c):
        c.execute(" SELECT * FROM USERS WHERE isStudent = 1")
        pprint(c.fetchall())

    # get all professors
    def getProfessor(conn,c):
        c.execute(" SELECT * FROM USERS WHERE isStudent = 0")
        pprint(c.fetchall())

    def __repr__(self):
        return f"Users('{self.fname}','{self.lname}','{self.userid}','{self.dept}','{self.rollno}','{self.phoneno}','{self.isStudent}')"

#################################################### ROOMS MODEL #################################################

class Rooms:

    def __init__(self, roomid, roomname, uid,id= None):
        self.id = id
        self.roomid = roomid
        self.roomname = roomname
        self.uid = uid
       

    # Insert Data Into table rooms
    def insert_rooms(room,conn,c):
        with conn:
            c.execute("INSERT INTO ROOMS(uid,roomid,roomname) VALUES(:uid,:roomid,:roomname)",{'uid':room.uid,'roomid': room.roomid,'roomname':room.roomname})
    
    # Delete Data from table rooms
    def delete_rooms(room,conn,c):
        with conn:
            c.execute("DELETE from ROOMS WHERE roomid = :roomid",{'roomid': room.roomid})

    # Update Data Into table rooms
    def update_rooms(room,conn,c):
        pass

    # get all rooms
    def getAllRooms(conn,c):
        c.execute(" SELECT * FROM ROOMS")
        pprint(c.fetchall())

    # get one room
    def getRoom(conn,room,c):
        with conn:
            c.execute(" SELECT * FROM ROOMS WHERE roomid = :roomid", {'roomid':room})
            pprint(c.fetchall())

    def __repr__(self):
        return f"Room('{self.id}','{self.roomid}','{self.uid}')"

#################################################### LOGS MODEL #################################################

class Logs:

    def __init__(self,userid,roomid,timein,timeout,srno=None):
        self.srno = srno
        self.userid = userid
        self.roomid = roomid
        self.timein = timein
        self.timeout = timeout

    # insert data to logs
    def insertDataToLog(conn,c,log):
        with conn:
            c.execute(" INSERT INTO LOG(uid,rid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout);",{'userid': log.userid,'roomid': log.roomid,'timein': log.timein,'timeout': log.timeout})

    # get all logs
    def getLogs(conn,c):
        with conn:
            c.execute("SELECT * FROM LOG")
            pprint(c.fetchall())

    def __repr__(self):
        return f"Logs('{self.userid}','{self.roomid}','{self.timein}','{self.timeout}')"

#################################################### ACCESS-MODEL MODEL #################################################

class Access_Control:

    def __init__(self,userid,roomid,timein=None,timeout=None,srno=None):
        self.srno = srno
        self.userid = userid
        self.roomid = roomid
        self.timein = timein
        self.timeout = timeout

    #insert data to table access_system
    def insert_access_control(ac,conn,c):
        with conn:
            c.execute("INSERT INTO ACCESS_CONTROL(userid,roomid) VALUES(:userid,:roomid)",{'userid':ac.userid,'roomid':ac.roomid})
            # c.execute("INSERT INTO ACCESS_CONTROL(userid,roomid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout)",{'userid':ac.userid,'roomid':ac.roomid,'timein': ac.timein,'timeout': ac.timeout})


    # display all data
    def getAllACData(conn,c):
        with conn:
            c.execute("SELECT * FROM ACCESS_CONTROL")
            pprint(c.fetchall())


2220200210,'Shinde', 'U',"shinde", 24,'extc',456879213,0