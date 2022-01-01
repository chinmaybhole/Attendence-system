from flask import Blueprint

application = Blueprint("application",__name__,static_folder="static",template_folder="templates")


@application.route("/test")
def test():
    return "test"