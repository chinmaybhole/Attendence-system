from datetime import datetime
from enum import unique
# from logging import NullHandler, setLogRecordFactory
from flask import Flask, Blueprint
from App.application import application
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3

app = Flask(__name__) # name of the flask application
app.register_blueprint(application,url_prefix= "")
app.config['SQLITE_DATABASE_URI'] = 'sqlite:///site.db'

db = sqlite3(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    uid = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(20), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return f"Users('{self.uid}','{self.name}')"

class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    room_id = db.Column(db.Integer, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    time_in = db.Column(db.DateTime, nullable= False, default = datetime.utcnow)
    time_out = db.Column(db.DateTime, nullable= False, default = datetime.utcnow)

    def __repr__(self):
        return f"Users('{self.id}','{self.room_id}','{self.user_id}','{self.time_in}','{self.time_out}')"

class Logs(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    room_id = db.relationship('Rooms.id',lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    time_in = db.relationship('Rooms.time_in',lazy=True)
    time_out = db.relationship('Rooms.time_out',lazy=True)

    def __repr__(self):
        return f"Users('{self.id}','{self.room_id}','{self.user_id}','{self.time_in}','{self.time_out}')"

@app.route("/")
def dashboard():
    return "<h1>Access Application (SERVER)</h1>"

@app.route("/rooms")
def rooms():
    return "rooms"

# swagger UI

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# end of swagger ui

if __name__ =="__main__":
    app.run(debug=True)

