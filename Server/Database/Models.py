import datetime
from os import access
from pprint import pprint 

#################################################### USERS MODEL #################################################

class Users:

    def __init__(self, userid, fname, lname, passw, dept, phoneno, isStudent,rollno=None, div=None,srno=None):
        self.srno = srno
        self.fname = fname
        self.lname = lname
        self.passw = passw
        self.userid = userid
        self.dept = dept
        self.rollno = rollno
        self.div = div
        self.phoneno = phoneno
        self.isStudent = isStudent

    def insert_user(user,conn,c):
        with conn:
            c.execute("INSERT INTO USERS(userid,fname,lname,passw,rollno,div,dept,phone,isStudent) VALUES(:userid,:fname,:lname,:passw,:rollno,:div,:dept,:phoneno,:isStudent)",{'userid': user.userid,'fname': user.fname,'lname': user.lname,'passw':user.passw,'rollno': user.rollno,'div':user.div,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent})

    # Delete Data of table user
    def delete_user(user,conn,c):
        with conn:
            c.execute("DELETE from USERS WHERE userid = :userid",{'userid': user.userid})

    # Update Data of table user
    def update_user(user,conn,c):
        with conn:
            c.execute(""" UPDATE USERS SET fname = :fname AND lname = :lname AND userid = :userid
                    WHERE id = :id""",{':userid':user.userid,'id': user.srno, 'fname': user.fname, 'lname': user.lname})

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
       profid =  c.execute(" SELECT * FROM USERS WHERE isStudent = 0")

        # pprint(c.fetchall())

    def __repr__(self):
        return f"Users('{self.fname}','{self.lname}','{self.userid}','{self.dept}','{self.rollno}','{self.phoneno}','{self.isStudent}')"

#################################################### ROOMS MODEL #################################################

class Rooms:

    def __init__(self, roomno, roomname):
        self.roomno = roomno
        self.roomname = roomname
       

    # Insert Data Into table rooms
    def insert_rooms(room,conn,c):
        with conn:
            c.execute("INSERT INTO ROOMS(roomno,roomname) VALUES(:roomno,:roomname);",{'roomno': room.roomno,'roomname':room.roomname})
    
    # Delete Data from table rooms
    def delete_rooms(room,conn,c):
        with conn:
            c.execute("DELETE FROM ROOMS WHERE roomno = :roomno",{'roomno': room.roomno})

    # Update Data Into table rooms
    def update_rooms_no(room,conn,c):
        with conn:
            c.execute("UPDATE ROOMS SET roomno = :roomno WHERE roomname = :roomname",{'roomno':room.roomno,'roomname':room.roomname})

    # get all rooms
    def getAllRooms(conn,c):
        c.execute(" SELECT * FROM ROOMS")
        pprint(c.fetchall())

    # get one room
    def getRoom(conn,room,c):
        with conn:
            c.execute(" SELECT * FROM ROOMS WHERE roomno = :roomno", {'roomno':room})
            pprint(c.fetchall())

    def __repr__(self):
        return f"Room('{self.id}','{self.roomno}','{self.uid}')"

#################################################### LOGS MODEL #################################################

class Logs:

    def __init__(self,access_srno,timein=None,timeout=None,srno=None):
        self.srno = srno
        self.access_srno = access_srno
        self.timein = timein
        self.timeout = timeout

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
    def getAllLogs(conn,c):
        with conn:
            c.execute("SELECT * FROM LOGS")
            pprint(c.fetchall())
    


    def __repr__(self):
        return f"Logs('{self.userid}','{self.roomid}','{self.timein}','{self.timeout}')"

#################################################### ACCESS-MODEL MODEL #################################################

class Access_Control:

    def __init__(self,roomno,userid=None,profid=None,srno=None):
        self.srno = srno
        self.userid = userid
        self.roomno = roomno
        self.profid = profid

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
            # c.execute("INSERT INTO ACCESS_CONTROL(userid,roomid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout)",{'userid':ac.userid,'roomid':ac.roomid,'timein': ac.timein,'timeout': ac.timeout})


    # display all data
    def getAllACData(conn,c):
        with conn:
            c.execute("SELECT * FROM ACCESS_CONTROL")
            pprint(c.fetchall())

    # update the timeout if timein exists 
    def update_access_data(data,conn,c):
        with conn:
            c.execute("UPDATE ACCESS_CONTROL SET old.timeout= new.timeout WHERE timein")


#############################################################################################################################

# import datetime
# from pprint import pprint 

# #################################################### USERS MODEL #################################################

# class Users:

#     def __init__(self, userid, fname, lname, passw, rollno, div, dept, phoneno, isStudent,srno=None):
#         self.srno = srno
#         self.fname = fname
#         self.lname = lname
#         self.passw = passw
#         self.userid = userid
#         self.dept = dept
#         self.rollno = rollno
#         self.div = div
#         self.phoneno = phoneno
#         self.isStudent = isStudent

#     def insert_user(user,conn,c):
#         with conn:
#             c.execute("INSERT INTO USERS(userid,fname,lname,passw,rollno,div,dept,phone,isStudent) VALUES(:userid,:fname,:lname,:passw,:rollno,:div,:dept,:phoneno,:isStudent)",{'userid': user.userid,'fname': user.fname,'lname': user.lname,'passw':user.passw,'rollno': user.rollno,'div':user.div,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent})

#     # Delete Data of table user
#     def delete_user(user,conn,c):
#         with conn:
#             c.execute("DELETE from USERS WHERE userid = :userid",{'userid': user.userid})

#     # Update Data of table user
#     def update_user(user,conn,c):
#         with conn:
#             c.execute(""" UPDATE USERS SET fname = :fname AND lname = :lname AND userid = :userid
#                     WHERE id = :id""",{':userid':user.userid,'id': user.srno, 'fname': user.fname, 'lname': user.lname})

#     # get all users
#     def getAllUsers(conn,c):
#         c.execute(" SELECT * FROM USERS")
#         pprint(c.fetchall())

#     # get all students
#     def getStudent(conn,c):
#         c.execute(" SELECT * FROM USERS WHERE isStudent = 1")
#         pprint(c.fetchall())

#     # get all professors
#     def getProfessor(conn,c):
#         c.execute(" SELECT * FROM USERS WHERE isStudent = 0")
#         pprint(c.fetchall())

#     def __repr__(self):
#         return f"Users('{self.fname}','{self.lname}','{self.userid}','{self.dept}','{self.rollno}','{self.phoneno}','{self.isStudent}')"

# #################################################### ROOMS MODEL #################################################

# class Rooms:

#     def __init__(self, roomno, roomname, uid, profid,id= None):
#         self.id = id
#         self.roomno = roomno
#         self.roomname = roomname
#         self.uid = uid
#         self.profid = profid
       

#     # Insert Data Into table rooms
#     def insert_rooms(room,conn,c):
#         with conn:
#             c.execute("INSERT INTO ROOMS(profid,roomno,roomname) VALUES(:profid,:roomno,:roomname);",{'profid':room.profid,'roomno': room.roomno,'roomname':room.roomname})
    
#     # Delete Data from table rooms
#     def delete_rooms(room,conn,c):
#         with conn:
#             c.execute("DELETE FROM ROOMS WHERE roomno = :roomno",{'roomno': room.roomno})

#     # Update Data Into table rooms
#     # def update_rooms(room,conn,c):
#     #     with conn:
#     #         c.execute("UPDA")

#     # get all rooms
#     def getAllRooms(conn,c):
#         c.execute(" SELECT * FROM ROOMS")
#         pprint(c.fetchall())

#     # get one room
#     def getRoom(conn,room,c):
#         with conn:
#             c.execute(" SELECT * FROM ROOMS WHERE roomno = :roomno", {'roomno':room})
#             pprint(c.fetchall())

#     def trigger_update_student(uid,conn,c):
#         with conn:
#             c.execute("UPDATE ROOMS SET uid = :uid|| WHERE roomno = :roomno",{'uid':Rooms.uid,'roomno':Rooms.roomno})

#     def __repr__(self):
#         return f"Room('{self.id}','{self.roomno}','{self.uid}')"

# #################################################### LOGS MODEL #################################################

# class Logs:

#     def __init__(self,userid,roomid,timein,timeout,srno=None):
#         self.srno = srno
#         self.userid = userid
#         self.roomid = roomid
#         self.timein = timein
#         self.timeout = timeout

#     def insert_trigger(conn,c):
#         with conn:
#             c.execute("""CREATE TRIGGER IF NOT EXISTS logs_trigger
#                         AFTER INSERT ON ACCESS_CONTROL
#                         WHEN new.timein AND new.timeout IS NOT NULL
#                         BEGIN
#                             INSERT INTO LOGS(LOGS_uid,LOGS_roomno,LOGS_timein,LOGS_timeout) VALUES(new.userid,new.rid,new.timein,new.timeout);
#                         END;
#                     """)

#     # insert data to logs
#     def insertDataToLog(conn,c,log):
#         with conn:
#             c.execute(" INSERT INTO LOGS(uid,rid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout);",{'userid': log.userid,'roomid': log.roomid,'timein': log.timein,'timeout': log.timeout})

#     # get all logs
#     def getLogs(conn,c):
#         with conn:
#             c.execute("SELECT * FROM LOGS")
#             pprint(c.fetchall())
    


#     def __repr__(self):
#         return f"Logs('{self.userid}','{self.roomid}','{self.timein}','{self.timeout}')"

# #################################################### ACCESS-MODEL MODEL #################################################

# class Access_Control:

#     def __init__(self,userid,rid,timein=None,timeout=None,srno=None):
#         self.srno = srno
#         self.userid = userid
#         self.rid = rid
#         self.timein = timein
#         self.timeout = timeout

#     # def timein_timeout_check(timein, timeout):
#     #     if timein >= timeout:
#     #         pass

#     #insert data to table access_system
#     def insert_access_control(ac,conn,c):
#         with conn:
#             c.execute("INSERT INTO ACCESS_CONTROL(userid,rid) VALUES(:userid,:rid)",{'userid':ac.userid,'rid':ac.rid})
#             # c.execute("INSERT INTO ACCESS_CONTROL(userid,roomid,timein,timeout) VALUES(:userid,:roomid,:timein,:timeout)",{'userid':ac.userid,'roomid':ac.roomid,'timein': ac.timein,'timeout': ac.timeout})


#     # display all data
#     def getAllACData(conn,c):
#         with conn:
#             c.execute("SELECT * FROM ACCESS_CONTROL")
#             pprint(c.fetchall())

#     # update the timeout if timein exists 
#     def update_access_data(data,conn,c):
#         with conn:
#             c.execute("UPDATE ACCESS_CONTROL SET old.timeout= new.timeout WHERE timein")


