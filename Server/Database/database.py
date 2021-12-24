import sqlite3
import sys
from Models import *
from pprint import pprint

conn = sqlite3.connect('Access_Control.sqlite')
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")

user1 =  Users(2220200309,'Abbas', 'A',"abbas", 1,'extc',132468579,1)
room = Rooms(801,"physics lab",1)

ac = Access_Control(1,801)

log = Logs(2220200309,801,"12:41","1:45")



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
        dept TEXT NOT NULL,
        phone TEXT NOT NULL,
        isStudent INTEGER NOT NULL
    ); ''')

except sqlite3.OperationalError :
    pass

    # Insert Data into table user
    # Users.insert_user(user1,conn,c)

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
            roomid INTEGER NOT NULL, 
            roomname TEXT NOT NULL,
            uid INTEGER NOT NULL,
            FOREIGN KEY(uid) 
            REFERENCES USERS(id)
        );
    """)
    
    
except sqlite3.OperationalError :
    pass
    
    # Insert Data Into table rooms
    # Rooms.insert_rooms(room,conn,c)  

    # Delete Data from table rooms
    # Rooms.delete_rooms(room,conn)

    # Update Data Into table rooms
    # Rooms.update_rooms(room)

#################################################### TABLE ACCESS_CONTROL #################################################



try:
    # pass
    c.execute("""CREATE TABLE ACCESS_CONTROL
        (
            srno INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            timein TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            timeout TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            userid INTEGER NOT NULL,
            roomid INTEGER NOT NULL,
            FOREIGN KEY(userid) 
            REFERENCES USERS(id)
        );
    """)
    # FOREIGN KEY(roomid) 
    #         REFERENCES ROOMS(rid),
    

except sqlite3.OperationalError :
    pass

    # Insert data into Access_control
    # Access_Control.insert_access_control(ac,conn,c)
        
    # Delete data from Access_control

    # Update data into Access_control



##################################################### TABLE LOGS ################################################

try:
    # Create Table Log
    c.execute("""CREATE TABLE LOGS AS 
                SELECT USERS.id AS 'LOGS_uid',
                ROOMS.roomid AS 'LOGS_roomno',
                ACCESS_CONTROL.timein AS 'LOGS_timein',
                ACCESS_CONTROL.timeout AS 'LOGS_timeout'
                FROM USERS,ROOMS,ACCESS_CONTROL
                WHERE USERS.id = ROOMS.uid
                AND ACCESS_CONTROL.timein AND ACCESS_CONTROL.timeout IS NOT NULL;
    );
""")
    # c.execute("""
    #     CREATE TABLE LOG AS 
    #     SELECT
    # """)
except sqlite3.OperationalError :
    pass

    # Logs.insertDataToLog(conn,c,log)
#     CREATE TABLE demo(
#   id INT PRIMARY KEY,
#   time_in DATETIME DEFAULT CURRENT_TIME
#   );
  
#   INSERT INTO demo(id) VALUES(1);

##################################################### TABLE ENDS ################################################

user2 =  Users('Shinde', 'D', 2220200310,'extc',1,132468579,0,1)
user3 =  Users('Chinmay', 'B', 2220200309,'extc',1,132468579,1,0)
user4 =  Users('Yash', 'S', 2220200309,'extc',1,132468579,1,0)
user5 =  Users('Aniket', 'G', 2220200309,'extc',1,132468579,1,0)
user6 =  Users('Kavita', 'C', 2220200310,'extc',1,132468579,0,1)



room1 = Rooms(802,"11:20","13:20")
room2 = Rooms(803,"12:20","15:20")
room3 = Rooms(804,"14:10","17:20")


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
c.execute("""SELECT * FROM ROOMS WHERE USERS.id = ROOMS.uid
""")
pprint(c.fetchall())



conn.close()


  