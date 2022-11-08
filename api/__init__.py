'''
Api folder keeps track of all config
Like Route, Resource, Database
This folder is then exported to app.py
where app.py will be able to run flask framework

'''


from flask import Flask
from flask_restful import Api


app = Flask(__name__)

api = Api(app)

from routes.home_route import HomeRoute
from routes.pdf_route import PDFRoute

api.add_resource(HomeRoute,"/")
api.add_resource(PDFRoute, "/pdf")