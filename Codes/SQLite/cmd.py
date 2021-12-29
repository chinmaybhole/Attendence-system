import sys
import sqlite3
import string
from random import randint
from pprint import pprint
import os
from hashlib import pbkdf2_hmac
from cmdFunc import hash_passwd

## Take uid and password as a argument from user
# uid =  sys.argv[1]
# passw = sys.argv[2]
# print(type(uid),type(passw))
# passw = hash_passwd(passw)

# Dummy data
uid = 222020008
passw = '6de8499a20d979b6fd3e0ee43c491b86924eb00cf8b34a43945f16e0038855f0'

## Connect the database
conn = sqlite3.connect("C:/Users/91703/Desktop/Access_Control.db")
## Cursor for database
cur = conn.cursor()
## UPDATE VALUES
cur.execute("""UPDATE USERS
            SET isStudent = 0
            WHERE id = 127""")
conn.commit()
cur.execute("select * from USERS")
pprint(cur.fetchall())
for i,j,k in cur.execute('SELECT userid,passw,isStudent FROM users'):
    # print(i,j,k)
    if i == int(uid): # and j == passw
        if k == 0:
            if j == passw:            
                # Id and Password checked
                # Now display the we need to zip the timestamps,usersid,lname,fname namelogs
                print("Ok")
            else:
                print('Wrong Password')
        else:
            print("You are not authorised")


# # # Check user in database 

