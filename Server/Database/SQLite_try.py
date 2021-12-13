import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")

# creation of Table

# conn.execute('''CREATE TABLE USERS 
# (ID INT PRIMARY KEY NOT NULL,
# UID INT NOT NULL,
# NAME TEXT NOT NULL,
# DEPT TEXT NOT NULL,
# PHONE TEXT
#       ); ''')
# print ("Table created successfully")

# Insert data into table "USERS"

conn.execute(''' INSERT INTO USERS (ID,UID,NAME,DEPT,PHONE) VALUES (1, 2220200309, 'ABBAS','EXTC',123467869 )''')
conn.execute(''' INSERT INTO USERS (ID,UID,NAME,DEPT,PHONE) VALUES (2, 2220200310, 'CHINMAY','EXTC',846513289 )''')
conn.execute(''' INSERT INTO USERS (ID,UID,NAME,DEPT,PHONE) VALUES (3, 2220200311, 'YASH','EXTC',458779846 )''')

conn.commit()
print("Records created Successfully")

# printing attributes of table "USERS"

cursor = conn.execute("SELECT * from USERS")
for row in cursor:
      print("ID = ",row[0])
      print("UID = ",row[1])
      print("NAME = ",row[2])
      print("DEPT = ",row[3])
      print("PHONE = ",row[4])

conn.execute("DROP TABLE USERS")



# #Updation in Database

# #Deletion
# #conn.execute("DELETE from COMPANY where ID = 2;")
# conn.execute("UPDATE COMPANY set SALARY = 54000 where ID = 1")
# conn.execute("UPDATE COMPANY set SALARY = 56000 where ID = 2")
# conn.execute("UPDATE COMPANY set SALARY = 60000 where ID = 3")
# conn.execute("UPDATE COMPANY set SALARY = 50000.0 where ID = 4")
# conn.commit()
# print("Total number of rows updated :" ,conn.total_changes)

# cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
# for row in cursor:
#    print("ID = ", row[0])
#    print("NAME = ", row[1])
#    print("ADDRESS = ", row[2])
#    print("SALARY = ", row[3])

# print("Operation done successfully")
# conn.execute("DROP TABLE test")
conn.close()