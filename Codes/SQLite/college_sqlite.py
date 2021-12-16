import sqlite3
conn = sqlite3.connect('college.sqlite ')


cur = conn.cursor()
#Before creating table, drop if it exists
'''
cur.execute('DROP TABLE IF EXISTS user')
##Create table department
cur.execute("""CREATE TABLE user
    (
    SrNo INTEGER NOT NULL PRIMARY KEY,
    Uid INTEGER NOT NULL,
	name TEXT NOT NULL,
    Dept TEXT,
    phoneNo TEXT	
    )
""")"""
"""
cur.execute('DROP TABLE IF EXISTS access_control')
##Create table department
cur.execute("""CREATE TABLE access_control
    (
	roomId TEXT NOT NULL,
 	sno INTEGER NOT NULL,
    FOREIGN KEY (SNo) REFERENCES user (SrNo)
    )
""")
cur.execute('DROP TABLE IF EXISTS room')
##Create table department
cur.execute("""CREATE TABLE room
    (
	tsrno TEXT NOT NULL PRIMARY KEY,
    roomname TEXT NOT NULL,
    tin INTEGER NOT NULL,
    tout INTEGER NOT NULL,
 	uid INTEGER NOT NULL,
    FOREIGN KEY (uid) REFERENCES user (SrNo)
    )
""")'''
cur.execute('DROP TABLE IF EXISTS logs')
##Create table department
cur.execute("""CREATE TABLE logs
    (
	tsrno TEXT NOT NULL PRIMARY KEY,
    roomname TEXT NOT NULL,
    tin INTEGER NOT NULL,
    tout INTEGER NOT NULL,
 	uid INTEGER NOT NULL,
    FOREIGN KEY (uid) REFERENCES user (SrNo)
    )
""")

##cur.execute('DROP TABLE IF EXISTS department')
##Create table department
#cur.execute("""CREATE TABLE department
#    (
#	name TEXT NOT NULL,
# 	deptno INTEGER NOT NULL PRIMARY KEY
#    )
#""")

##Before creating table, drop if it exists
#cur.execute('DROP TABLE IF EXISTS employee')
#
##Create table department
#
#cur.execute("""CREATE TABLE employee
#	(
#		name TEXT NOT NULL,
#		ssn TEXT NOT NULL PRIMARY KEY,
#		bdate TEXT,
#		address TEXT,
#		salary INTEGER CHECK(salary > 1000),
#		dno INTEGER NOT NULL,
#		FOREIGN KEY (dno) REFERENCES department (deptno)
#	)
#   """)

#Before creating table, drop if it exists
#cur.execute('DROP TABLE IF EXISTS deptlocations')
#
##Create table deptlocations
#cur.execute("""CREATE TABLE deptlocations
#	(
#		dnumber INTEGER NOT NULL,
#		dlocation TEXT NOT NULL,
#		PRIMARY KEY (dnumber, dlocation),
#		FOREIGN KEY (dnumber) REFERENCES department (deptno)
#	)
#""")

#Create table project
#
# cur.execute("""CREATE TABLE project
#
# 	(
#
# 		pname TEXT NOT NULL,
#
# 		pnumber INTEGER NOT NULL,
#
# 		plocation TEXT NOT NULL,
#
# 		dnum INTEGER NOT NULL,
#
# 		PRIMARY KEY (pnumber, plocation),
#
# 		FOREIGN KEY (dnum) REFERENCES department (deptno)
#
# 	)
#
# """)
#
# #Before creating table, drop if it exists
#
# cur.execute('DROP TABLE IF EXISTS works_on')
#

#
# #Create table works_on
#
# cur.execute("""CREATE TABLE works_on
#
# 	(
#
# 		essn TEXT NOT NULL,
#
# 		pno INTEGER NOT NULL,
#
# 		hour INTEGER NOT NULL,
#
# 		PRIMARY KEY(essn,pno),
#
# 		FOREIGN KEY (essn) REFERENCES project (employee),
#
# 		FOREIGN KEY (pno) REFERENCES project (pnumber)
#
# 	)
#
# """)
#

#cur.execute("""ALTER TABLE department
#          ADD COLUMN mgr_ssn TEXT REFERENCES employee(ssn);
#""")

