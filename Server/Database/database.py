from os import pardir
import sqlite3
import sys
from Models import *
from pprint import pprint

conn = sqlite3.connect('Access_Control.sqlite')
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")

# user1 =  Users(2220200309,"Abbas","A","abbas",1,"A","extc",1234657980,1)
user2 =  Users(2220200309,"Chinmay","B","chinmay",10,"A","extc",4657987123,1)
# user3 =  Users(2220200310,"Yash","S","yash",51,"A","extc",1324689798,1)
# user4 =  Users(2220200310,"Yash","S","yash",51,"A","extc",1324689798,1)

# user = [Users(2220200309,"Abbas","A","abbas",1,"A","extc",1234657980,1),
#         Users(2220200309,"Chinmay","B","chinmay",10,"A","extc",4657987123,1),
#         Users(2220200310,"Yash","S","yash",51,"A","extc",1324689798,1),
#         Users(2220200311,"ABC","Z","abc",20,"B","extc",4567981320,1)]

# room1 = Rooms(801,"physics lab",1)
room2 = Rooms(801,"physics lab",2)
# room3 = Rooms(801,"physics lab",3)

# room = [Rooms(801,"physics lab",1),
#         Rooms(801,"physics lab",2),
#         Rooms(801,"physics lab",3),
#         Rooms(802,"language lab",4)]


# ac1 = Access_Control(1,1)
ac2 = Access_Control(2,1)
# ac3 = Access_Control(3,801)

# ac = [Access_Control(1,801),
#     Access_Control(2,801),
#     Access_Control(3,801),
#     Access_Control(4,802)]


# log = Logs(2220200309,801,"12:41","1:45")



# drop table if exists
# c.execute('DROP TABLE IF EXISTS users')
# c.execute('DELETE FROM room')
# c.execute('DROP TABLE access_control')


#################################################### TABLE USERS #################################################

try:
#     # create table Users
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
        phone TEXT NOT NULL,
        isStudent INTEGER NOT NULL
    ); ''')

except sqlite3.OperationalError :
    pass

    # Insert Data into table user
    # Users.insert_user(user2,conn,c)

    # Delete Data of table user
    # Users.delete_user(user1,conn)

    # Update Data of table user
    # Users.update_user(user1,conn)

##################################################### TABLE ROOMS ################################################
try:
    # pass
    #Create table Room
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
    
    
except sqlite3.OperationalError :
    pass
    
    # Insert Data Into table rooms
    # Rooms.insert_rooms(room2,conn,c)  

    # Delete Data from table rooms
    # Rooms.delete_rooms(room,conn)

    # Update Data Into table rooms
    # Rooms.update_rooms(room)

#################################################### TABLE ACCESS_CONTROL #################################################



try:
    # pass
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
    # FOREIGN KEY(userid) 
    #         REFERENCES USERS(id)
    # FOREIGN KEY(rno)
    #         REFERENCES ROOMS(roomno)

except sqlite3.OperationalError :
    # pass

    # Insert data into Access_control
    Access_Control.insert_access_control(ac2,conn,c)

    # c.execute("INSERT INTO ACCESS_CONTROL(userid,rno,timein,timeout) VALUES(1,801,'22-12-2021 00:00:00','22-12-2021 00:09:00')")

        
    # Delete data from Access_control

    # Update data into Access_control



##################################################### TABLE LOGS ################################################

try:
    # pass
    # Create Table Log
    c.executescript("""CREATE TABLE LOGS AS 
                SELECT USERS.userid AS 'LOGS_uid',
                ROOMS.roomno AS 'LOGS_roomno',
                ACCESS_CONTROL.timein AS 'LOGS_timein',
                ACCESS_CONTROL.timeout AS 'LOGS_timeout'
                FROM USERS,ROOMS,ACCESS_CONTROL
                WHERE USERS.id = ROOMS.uid
                AND ACCESS_CONTROL.timein AND ACCESS_CONTROL.timeout IS NOT NULL;
                """)
 
except sqlite3.OperationalError :
    pass
    # Logs.insert_trigger(conn,c)
  

##################################################### TABLE ENDS ################################################

# user2 =  Users('Shinde', 'D', 2220200310,'extc',1,132468579,0,1)
# user3 =  Users('Chinmay', 'B', 2220200309,'extc',1,132468579,1,0)
# user4 =  Users('Yash', 'S', 2220200309,'extc',1,132468579,1,0)
# user5 =  Users('Aniket', 'G', 2220200309,'extc',1,132468579,1,0)
# user6 =  Users('Kavita', 'C', 2220200310,'extc',1,132468579,0,1)



# room1 = Rooms(802,"11:20","13:20")
# room2 = Rooms(803,"12:20","15:20")
# room3 = Rooms(804,"14:10","17:20")


# insert_user(user1)
# insert_user(user2)
# insert_user(user3)
# insert_user(user4)
# insert_user(user5)
# insert_user(user6)

# insert_rooms(room)
# insert_rooms(room1)
# insert_rooms(room2)
# insert_rooms(room3)


#print(arg1,arg2,arg3)

conn.commit()

##################################################### GET DATA ################################################

# Users.getAllUsers(conn,c)

# Users.getStudent(conn)

# Users.getProfessor(conn)

# Rooms.getAllRooms(conn,c)

# Rooms.getRoom(conn,801,c)

# Access_Control.getAllACData(conn,c)

# Logs.getLogs(conn,c)

##################################################### DISPLAY DATA ################################################

# getAllRooms()
# getAllUsers()
# c.execute("SELECT * FROM USERS")
# pprint(c.fetchall())
# c.execute("""SELECT * FROM ROOMS WHERE USERS.id = ROOMS.uid
# """)
# pprint(c.fetchall())



conn.close()


  
