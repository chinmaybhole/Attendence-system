import sqlite3
import sys
from Models import *
from pprint import pprint

conn = sqlite3.connect(':memory:')
c = conn.cursor()

# drop table if exists
# c.execute('DROP TABLE IF EXISTS room')

#################################################### TABLE ACCESS_CONTROL #################################################


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

# Insert data into Access_control
# def insert_access_control(ac):
#     with conn:
#         c.execute("INSERT INTO access_control(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user.uid,'fname': user.fname,'lname': user.lname,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent,'isProfessor': user.isProfessor})


# Delete data from Access_control

# Update data into Access_control



## CRUD OPERARIONS

#################################################### TABLE USERS #################################################

# create table Users
conn.execute('''CREATE TABLE users 
(
    id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
    uid integer NOT NULL,
    fname text NOT NULL,
    lname text NOT NULL,
    dept text NOT NULL,
    phone text NULL,
    isStudent int NOT NULL,
    isProfessor int NOT NULL
); ''')

# Insert Data into table user
def insert_user(user):
    with conn:
        c.execute("INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user.uid,'fname': user.fname,'lname': user.lname,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent,'isProfessor': user.isProfessor})

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

# c.execute("INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user1.uid,'fname': user1.fname,'lname': user1.lname,'dept':user1.dept,'phoneno': user1.phoneno,'isStudent': user1.isStudent,'isProfessor': user1.isProfessor})

# c.execute(f"INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES({user2.uid},{user2.fname},{user2.lname},{user2.dept},{user2.phoneno},{user2.isStudent},{user2.isProfessor})")

# c.execute("DROP TABLE users")
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
# user1 =  Users('Abbas', 'A', 2220200309,'extc',1,132468579,1,0)
# user2 =  Users('ABC', 'D', 2220200310,'extc',1,132468579,0,1)
room = Rooms(arg1,arg2,arg3)

# insert_user(user1)
# insert_user(user2)
insert_rooms(room)

#print(arg1,arg2,arg3)

conn.commit()

c.execute("SELECT * from users")
pprint(c.fetchall())

c.execute("SELECT * from room")
pprint(c.fetchall())

conn.close()

