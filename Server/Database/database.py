import sqlite3
import sys
from Models import *
from pprint import pprint

conn = sqlite3.connect('Access_System.db')
c = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")

user1 =  Users(2220200309,'Abbas', 'A',"abbas", 1,'extc',132468579,1)
room = Rooms(801,"phy",1)

ac = Access_Control("12:41","1:45",1)



# drop table if exists
# c.execute('DROP TABLE IF EXISTS users')
# c.execute('DELETE FROM room')
# c.execute('DROP TABLE access_control')


#################################################### TABLE USERS #################################################

try:
    # create table Users
    conn.execute('''CREATE TABLE IF NOT EXISTS USERS
    (
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid integer NOT NULL,
        fname text NOT NULL,
        lname text NOT NULL,
        passw text NOT NULL,
        dept text NOT NULL,
        phone text NOT NULL,
        isStudent int NOT NULL
    ) ''')

except sqlite3.OperationalError :
    pass

    # Insert Data into table user
    Users.insert_user(user1,conn,c)

    # Delete Data of table user
    # Users.delete_user(user1,conn)

    # Update Data of table user
    # Users.update_user(user1,conn)

##################################################### TABLE ROOMS ################################################
try:
    # pass
    #Create table Room
    c.execute("""CREATE TABLE IF NOT EXISTS ROOMS
        (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            roomid INTEGER NOT NULL,
            roomname TEXT NOT NULL,
            uid INTEGER NULL,
            FOREIGN KEY (uid) 
            REFERENCES USERS (id)
        )
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
    # Create table Access_Control
    c.execute("""CREATE TABLE IF NOT EXISTS ACCESS_CONTROL
        (
        srno integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        timein text not null,
        timeout text not null,
        userid INTEGER NULL,
        rid Integer NULL,
        FOREIGN KEY (userid) 
        REFERENCES USERS (uid),
        FOREIGN KEY (rid) 
        REFERENCES ROOMS (roomid)
        )
    """)

except sqlite3.OperationalError :
    pass

    # Insert data into Access_control
    Access_Control.insert_access_control(ac,conn,c)
        
    # Delete data from Access_control

    # Update data into Access_control



##################################################### TABLE LOGS ################################################

try:
    # Create Table Log
    c.execute("""CREATE TABLE IF NOT EXISTS LOG 
    ( 
        srno integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid integer NOT NULL,
        roomid integer NOT NULL,
        timein integer NOT NULL,
        timeout integer NOT NULL,
        FOREIGN KEY (timein) 
        REFERENCES ROOMS (timein),
        FOREIGN KEY (timeout) 
        REFERENCES ROOMS (timeout),
        FOREIGN KEY (uid) 
        REFERENCES USERS (uid),
        FOREIGN KEY (roomid) 
        REFERENCES ROOMS (roomid)
    )
""")
except sqlite3.OperationalError :
    pass

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

Users.getAllUsers(conn,c)

# Users.getStudent(conn)

# Users.getProfessor(conn)

Rooms.getAllRooms(conn,c)

# Rooms.getRoom(conn,801,c)

Access_Control.getAllACData(conn,c)

##################################################### DISPLAY DATA ################################################

# getAllRooms()
# getAllUsers()
# c.execute("SELECT * FROM room")
# pprint(c.fetchall())


conn.close()


  