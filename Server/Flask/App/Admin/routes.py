from flask import Blueprint

from flask_restx import Resource,Api,reqparse,Namespace

routes = Blueprint("routes",__name__)

namespace = Namespace('Admin', description= "All About Admin API's")

# @routes.route("/dashboard", methods=['GET'] )
class Dashboard(Resource):
    def get(self):
        return "dashboard"

class Download(Resource):
    def post(self):
        return "post download"


namespace.add_resource(Dashboard,'/dashboard')
namespace.add_resource(Download,'/download')
