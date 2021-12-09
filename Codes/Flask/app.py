from flask import Flask

app = Flask(__name__) # name of the flask application

@app.route("/")
def hello_world():
    return "esrdft"

if __name__ =="__main__":
    app.run(debug=True)

