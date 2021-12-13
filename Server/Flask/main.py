from flask import Flask, Blueprint
from App.application import application
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__) # name of the flask application
app.register_blueprint(application,url_prefix= "")




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

