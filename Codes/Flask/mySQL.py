import mysql.connector
db = mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="root",
    database="testdatabase"
)

mycursor = db.cursor()

#Creating a database
#mycursor.execute("CREATE DATABASE testdatabase") 