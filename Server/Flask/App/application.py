from flask import Blueprint, render_template

application = Blueprint("application",__name__,static_folder="static",template_folder="templates")

@application.route("/dashboard")
def test():
    return "dashboard"