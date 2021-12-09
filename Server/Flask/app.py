from flask import Flask

app = Flask(__name__) # name of the flask application

@app.route("/Dashboard")
def dashboard():
    return "dashboard"

@app.route("/rooms")
def rooms():
    return "rooms"

if __name__ =="__main__":
    app.run(debug=True)

