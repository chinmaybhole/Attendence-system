import sqlite3
import string
from random import randint
from pprint import pprint
import os
from hashlib import pbkdf2_hmac
# salt = os.urandom(32)
# print(salt)
salt=b'\x19G\xaf\x8d!\x82P\xac\x7f\xdc\xfc\xfbtRA\xa2OS\x9a\xc2\xd6\x0c\x91I\x8a2y\x1dM\x99\xf6\xbc'
# passwd = pbkdf2_hmac('sha256',b'chinmay123',salt,10)
# print(passwd.hex())
# passwd = bytes("Chinmay",'utf-8')

# passwd = pbkdf2_hmac('sha256',passwd,salt,10)
# print(passwd)

def random_phone_no(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

conn = sqlite3.connect("C:/Users/91703/Desktop/Access_Control.db")

cur = conn.cursor()
# cur.execute("DELETE FROM USERS")
# conn.commit()

############# DATA FILLING OF USER ###############
# for i,a in enumerate(string.ascii_lowercase[:10]):
#     # name = ['Chinmay','Abbas','Aathira','Yash','Aklant','Omkar','Saakshi','Samiksha','Akhila','Aniket']
#     # passwd = bytes(name[i],'utf-8')
#     # print(passwd)
#     # passwd = str(pbkdf2_hmac('sha256',passwd,salt,10).hex())
#     # print(passwd)
#     f_phone = random_phone_no(10)
#     pass
#     print(f_phone)
#     cur.execute("""INSERT INTO USERS(userid,fname,lname,passw,rollno,dept,phone,isStudent) VALUES(222020000+(000000001*:i),:name,:name_0,:passwd,70,'extc',:f_phone,1)""",{'i':i,'name':name[i],'name_0':name[i][0],'passwd':passwd,'f_phone':f_phone})
#     #conn.commit()
#print(len('222020000'))

# cur.execute("""INSERT INTO USERS(userid,fname,lname,passw,rollno,dept,phone,isStudent) VALUES(2220200311,'Yai','G','may',70,'extc',1324588526,1)""")
# conn.commit()
# cur.execute('SELECT id FROM USERS')
# li = list(map(lambda i: i[0],cur.fetchall()))
# # print(li)
# for i in li:
#      cur.execute("""INSERT INTO ROOMS(uid,roomno,roomname) VALUES(:uid,:roomno,:roomname)""",{'uid':i,'roomno': 801,'roomname':'physics'})
#      conn.commit()
    
# cur.execute("DELETE FROM ROOMS")
# #c.execute("INSERT INTO ROOMS(uid,roomid,roomname) VALUES(:uid,:roomid,:roomname)",{'uid':room.uid,'roomid': room.roomid,'roomname':room.roomname})
# cur.execute("SELECT * FROM ROOMS") 
# pprint(cur.fetchall())
cur.execute("SELECT * FROM ACCESS_CONTROL") 
pprint(cur.fetchall())
# conn.close()