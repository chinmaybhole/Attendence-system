import sqlite3
import sys
from Models import *
from pprint import pprint

conn = sqlite3.connect('test.sqlite')
c = conn.cursor()
c.execute("PRAGMA foreign_keys  = ON")

#################################################### TABLE USERS #################################################

# Create usertable
# sr: pk
# fname: not null
# lname: not null
# uid: not null (222)
# isStudent: bool (int 0 or 1)

try:
#     # create table Users
    c.execute('''CREATE TABLE USERS
    (
        srno INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
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
    # pass

    userS =  User(2220200309,"Abbas","A","abbas","extc",798465130,1,1,"A")
    userP =  User(2220200310,"ABC","Z","abc","extc",1327994561,0)


    # Insert Data into table user
    # Users.insert_user(userP,conn,c)

#################################################### TABLE ROOMS #################################################


# Create room table
# roomno: pk not null
# roomname: not null

try:
    # pass
    #Create table Room
    c.execute("""CREATE TABLE ROOMS
        (
            roomno INTEGER PRIMARY KEY NOT NULL,
            roomname TEXT NOT NULL
        );
    """)
    
    
except sqlite3.OperationalError :
    pass

    room1 = Rooms(801,"phy lab")
    room2 = Rooms(802,"lang lab")

    # Rooms.insert_rooms(room2,conn,c)

#################################################### TABLE ACCESS_CONTROL #################################################

# Create access_control table
# sr: pk
# uid: fk
# profid: (if isStudent == 0 so user uid is converted to profid)
# rid: fk

try:
    # pass
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

except sqlite3.OperationalError :
    pass

    ac1 = Access_Control(801,1,None)
    ac2= Access_Control(801,None,1)
    ac3= Access_Control(801,1,1)


    # Access_Control.insert_access_control(ac3,conn,c)

#################################################### TABLE LOGS #################################################

# Create log table
# timein: not null
# timeout: not null
# access_sr: pk

try:
    # pass
    # Create Table Log
    c.execute("""CREATE TABLE LOGS
                (
                srno INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                timein TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                timeout TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                access_srno INTEGER NOT NULL,
                FOREIGN KEY(access_srno) REFERENCES ACCESS_CONTROL(srno)
                );
            """)
 
except sqlite3.OperationalError :
    pass
    # log = Logs(1)
    # Logs.insertDataToLog(conn,c,log)
    # Logs.insert_trigger(conn,c)
  
##################################################### TABLE ENDS ################################################

conn.commit()

##################################################### DISPLAY TABLE DETAILS ################################################

# User.getAllUsers(conn,c)
User.getAUser(2220200309)

# Rooms.getAllRooms(conn,c)

# Access_Control.getAllACData(conn,c)

# Logs.getAllLogs(conn,c)

##################################################### DISPLAY TABLE DETAILS ENDS ################################################

conn.close()