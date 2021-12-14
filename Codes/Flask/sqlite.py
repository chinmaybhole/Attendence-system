import sqlite3
conn = sqlite3.connect('company.sqlite ')

cur = conn.cursor()
#Before creating table, drop if it exists

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

cur.execute("""ALTER TABLE department
          ADD COLUMN mgr_ssn TEXT REFERENCES employee(ssn);
""")

