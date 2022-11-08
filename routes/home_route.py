"""
an Initial HomeRoue

"""

from flask_restful import Resource
import json
from controller.home_controller import home


class HomeRoute(Resource):
    
    def get(self):
        return home()