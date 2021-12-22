import datetime
from pprint import pprint 


class Users:

    def __init__(self, uid, fname, lname, passw, rollno, dept, phoneno, isStudent,id=None):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.passw = passw
        self.uid = uid
        self.dept = dept
        self.rollno = rollno
        self.phoneno = phoneno
        self.isStudent = isStudent

    def insert_user(user,conn,c):
        with conn:
            c.execute("INSERT INTO USERS(uid,fname,lname,passw,dept,phone,isStudent) VALUES(:uid,:fname,:lname,:passw,:dept,:phoneno,:isStudent)",{'uid': user.uid,'fname': user.fname,'lname': user.lname,'passw':user.passw,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent})

    # Delete Data of table user
    def delete_user(user,conn,c):
        with conn:
            c.execute("DELETE from USERS WHERE uid = :uid",{'uid': user.uid})

    # Update Data of table user
    def update_user(user,conn,c):
        with conn:
            c.execute(""" UPDATE USERS SET fname = :fname AND lname = :lname AND uid = :uid
                    WHERE id = :id""",{':uid':user.uid,'id': user.id, 'fname': user.fname, 'lname': user.lname})

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
        return f"Users('{self.fname}','{self.lname}','{self.uid}','{self.dept}','{self.rollno}','{self.phoneno}','{self.isStudent}','{self.isProfessor}')"

class Rooms:

    def __init__(self, roomid, roomname, userid=None,id =None):
        self.id = id
        self.roomid = roomid
        self.userid = userid
        self.roomname= roomname
       

    # Insert Data Into table rooms
    def insert_rooms(room,conn,c):
        with conn:
            c.execute("INSERT INTO ROOMS(userid,roomid,roomname) VALUES(:userid,:roomid,:roomname)",{'roomid': room.roomid,'userid':room.userid,'roomname':room.roomname})
    
    # Delete Data from table rooms
    def delete_rooms(room,conn,c):
        with conn:
            c.execute("DELETE from ROOMS WHERE roomid = :roomid",{'roomid': room.roomid})

    # Update Data Into table rooms
    def update_rooms(room):
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
        return f"Room('{self.id}','{self.roomid}','{self.userid}','{self.timein}','{self.timeout}')"

class Logs:

    def __init__(self,userid,roomid,timein,timeout,srno=None):
        self.srno = srno
        self.userid = userid
        self.roomid = roomid
        self.timein = timein
        self.timeout = timeout

    # insert data to logs
    def insertDataToLog(conn,c,data):
        with conn:
            c.execute(" INSERT INTO LOG()")

    # get all logs
    def getLogs(conn,c):
        with conn:
            c.execute("SELECT * FROM LOG")
            pprint(c.fetchall())

    def __repr__(self):
        return f"Logs('{self.userid}','{self.roomid}','{self.timein}','{self.timeout}')"

class Access_Control:

    def __init__(self,timein,timeout,userid,srno=None,roomid=None):
        self.srno = srno
        self.userid = userid
        self.roomid = roomid
        self.timein = timein
        self.timeout = timeout

    #insert data to table access_system
    def insert_access_control(ac,conn,c):
        with conn:
            c.execute("INSERT INTO ACCESS_CONTROL(userid,timein,timeout) VALUES(:userid,:timein,:timeout)",{'userid':ac.userid,'timein': ac.timein,'timeout': ac.timeout})

    # display all data
    def getAllACData(conn,c):
        with conn:
            c.execute("SELECT * FROM access_control")
            pprint(c.fetchall())
