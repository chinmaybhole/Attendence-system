from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import mysql.connector


app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'nli1'
 
mysql = MySQL(app)
 
@app.route('/form')
def form():
    return render_template('home.html')
 
@app.route('/login', methods = ['POST', 'GET'])
def login(): 
 if request.method == "POST":
       
        no = request.form['number']
        name = request.form['name']

        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO tab1 VALUES(%s , %s)''',(no,name))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"

if __name__=="__main__":
    app.run(debug=True)
