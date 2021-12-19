import sqlite3
# from Models import *
from Models import Users

conn = sqlite3.connect(':memory:')
c = conn.cursor()


conn.execute('''CREATE TABLE users 
(id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
uid integer NOT NULL,
fname text NOT NULL,
lname text NOT NULL,
dept text NOT NULL,
phone text NULL,
isStudent int NOT NULL,
isProfessor int NOT NULL); ''')

user1 =  Users('Abbas', 'A', 2220200309,'extc',1,132468579,1,0)
user2 =  Users('ABC', 'D', 2220200310,'extc',1,132468579,0,1)

# print(user1.fname)
# print(user1.lname)
# print(user1.uid)

# print(user2.fname)
# print(user2.lname)
# print(user2.uid)

def insert_user(user):
    with conn:
        c.execute("INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user.uid,'fname': user.fname,'lname': user.lname,'dept':user.dept,'phoneno': user.phoneno,'isStudent': user.isStudent,'isProfessor': user.isProfessor})

def delete_user(user):
    with conn:
        c.execute("DELETE from users WHERE uid = :uid",{'uid': user.uid})

def update_user(user, uid):
    with conn:
        c.execute(""" UPDATE users SET fname = :fname AND lname = :lname 
                WHERE uid = :uid""",{'uid': user.uid, 'fname': user.fname, 'lname': user.lname})


# c.execute("INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES(:uid,:fname,:lname,:dept,:phoneno,:isStudent,:isProfessor)",{'uid': user1.uid,'fname': user1.fname,'lname': user1.lname,'dept':user1.dept,'phoneno': user1.phoneno,'isStudent': user1.isStudent,'isProfessor': user1.isProfessor})

# c.execute(f"INSERT INTO users(uid,fname,lname,dept,phone,isStudent,isProfessor) VALUES({user2.uid},{user2.fname},{user2.lname},{user2.dept},{user2.phoneno},{user2.isStudent},{user2.isProfessor})")

# c.execute("DROP TABLE users")

insert_user(user1)

conn.commit()

conn.close()


c.execute("SELECT * from users")


print(c.fetchall())

