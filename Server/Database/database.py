import sqlite3
import sys
from Models import *
from pprint import pprint

conn = sqlite3.connect('Access_Syetem.db')
c = conn.cursor()

# drop table if exists
# c.execute('DROP TABLE IF EXISTS users')
# c.execute('DELETE FROM room')
# c.execute('DROP TABLE room')



#################################################### TABLE ACCESS_CONTROL #################################################

try:
    # Create table Access_Control
    c.execute("""CREATE TABLE access_control
        (
        timein text not null,
        timeout text not null,
        userid INTEGER NOT NULL,
        roomid TEXT NOT NULL,
        FOREIGN KEY (userid) 
        REFERENCES users (uid),
        FOREIGN KEY (roomid) 
        REFERENCES room (roomid)
        )
    """)

except sqlite3.OperationalError :
    pass

    # Insert data into Access_control
    # def insert_access_control(ac):
    #     with conn:
    #         c.execute("INSERT INTO access_control(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user.uid,'fname': user.fname,'lname': user.lname,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent,'isProfessor': user.isProfessor})

    # Delete data from Access_control

    # Update data into Access_control



## CRUD OPERARIONS

#################################################### TABLE USERS #################################################

try:
    # create table Users
    conn.execute('''CREATE TABLE users 
    (
        id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid integer NOT NULL,
        fname text NOT NULL,
        lname text NOT NULL,
        passw text null,
        dept text NOT NULL,
        phone text NULL,
        isStudent int NOT NULL
    ) ''')

except sqlite3.OperationalError :

    # Insert Data into table user
    def insert_user(user):
        with conn:
            c.execute("INSERT INTO users(uid,fname,lname,passw,dept,phone,isStudent) VALUES(:uid,:fname,:lname,:passw,:dept,:phoneno,:isStudent)",{'uid': user.uid,'fname': user.fname,'lname': user.lname,'passw':user.passw,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent})

    # Delete Data of table user
    def delete_user(user):
        with conn:
            c.execute("DELETE from users WHERE uid = :uid",{'uid': user.uid})

    # Update Data of table user
    def update_user(user):
        with conn:
            c.execute(""" UPDATE users SET fname = :fname AND lname = :lname AND uid = :uid
                    WHERE id = :id""",{':uid':user.uid,'id': user.id, 'fname': user.fname, 'lname': user.lname})

##################################################### TABLE ROOMS ################################################
try:
    #Create table Room
    c.execute("""CREATE TABLE room
        (
            id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
            roomid INTEGER NULL,
            timein TEXT NOT NULL,
            timeout TEXT NOT NULL,
            uid INTEGER NULL,
            FOREIGN KEY (timeout) 
            REFERENCES access_control (timeout),
            FOREIGN KEY (uid) 
            REFERENCES user (id),
            FOREIGN KEY (timein) 
            REFERENCES access_control (timein)
        )
    """)
except sqlite3.OperationalError :

    # Insert Data Into table rooms
    def insert_rooms(room):
        with conn:
            c.execute("INSERT INTO room(roomid,timein,timeout) VALUES(:roomid,:timein,:timeout)",{'roomid': room.roomid,'timein':room.timein,'timeout':room.timeout})

    # Delete Data from table rooms
    def delete_rooms(room):
        with conn:
            c.execute("DELETE from users WHERE uid = :uid",{'uid': room.roomid})

    # Update Data Into table rooms
    def update_rooms(room):
        pass

##################################################### TABLE LOGS ################################################

try:
    # Create Table Log
    c.execute("""CREATE TABLE LOG 
    ( 
        srno integer PRIMARY KEY AUTOINCREMENT NOT NULL,
        uid integer NULL,
        roomid integer NULL,
        timein integer NOT NULL,
        timeout integer NOT NULL,
        FOREIGN KEY (timein) 
        REFERENCES room (timein),
        FOREIGN KEY (timeout) 
        REFERENCES room (timeout),
        FOREIGN KEY (uid) 
        REFERENCES users (uid),
        FOREIGN KEY (roomid) 
        REFERENCES room (roomid)
    )
""")
except sqlite3.OperationalError :
    pass

##################################################### TABLE ENDS ################################################

# c.execute("INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user1.uid,'fname': user1.fname,'lname': user1.lname,'dept':user1.dept,'phoneno': user1.phoneno,'isStudent': user1.isStudent,'isProfessor': user1.isProfessor})

# c.execute(f"INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES({user2.uid},{user2.fname},{user2.lname},{user2.dept},{user2.phoneno},{user2.isStudent},{user2.isProfessor})")

# c.execute("DROP TABLE users")
# arg1 = sys.argv[1]
# arg2 = sys.argv[2]
# arg3 = sys.argv[3]
user1 =  Users('Abbas', 'A', 2220200309,'extc',1,132468579,1,0)
user2 =  Users('Shinde', 'D', 2220200310,'extc',1,132468579,0,1)
user3 =  Users('Chinmay', 'B', 2220200309,'extc',1,132468579,1,0)
user4 =  Users('Yash', 'S', 2220200309,'extc',1,132468579,1,0)
user5 =  Users('Aniket', 'G', 2220200309,'extc',1,132468579,1,0)
user6 =  Users('Kavita', 'C', 2220200310,'extc',1,132468579,0,1)



room = Rooms(801,"19:20","20:20")
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

def getAllUsers():
    c.execute(" SELECT * FROM users")
    pprint(c.fetchall())

def getStudent():
    c.execute(" SELECT * FROM users WHERE isStudent = 1")
    pprint(c.fetchall())

def getProfessor():
    c.execute(" SELECT * FROM users WHERE isStudent = 0")
    pprint(c.fetchall())

def getAllRooms():
    c.execute(" SELECT * FROM room")
    pprint(c.fetchall())

def getRoom(room):
    c.execute(" SELECT * FROM room WHERE roomid = :roomid", {'roomid':room})
    pprint(c.fetchall())

##################################################### DISPLAY DATA ################################################

getAllRooms()
getAllUsers()


conn.close()


  