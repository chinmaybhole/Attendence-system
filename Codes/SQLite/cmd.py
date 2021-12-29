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
uid = 222020000
passw = '5c1c98889c958a98ffe5d4104bf943c71e0962e8ae5b2613a69cab19243384a4'

## Connect the database
conn = sqlite3.connect("C:/Users/91703/Desktop/Access_Control.db")
## Cursor for database
cur = conn.cursor()
cur.execute("select * from USERS")
pprint(cur.fetchall())
for i,j in cur.execute('SELECT userid,passw FROM users'):
    #print(i,j)
    if i == int(uid): # and j == passw
        if j == passw:            
            # Id and Password checked
            # Now display the timestamps,users namelogs
            pass
        else:
            print('Please enter the correct password')

# # # Check user in database 

