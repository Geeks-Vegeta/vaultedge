"""
an Initial HomeRoue

"""

from flask_restful import Resource, request
import json
from controller.pdf_controller import pdf, pdfbsf


class PDFRoute(Resource):
    
    def post(self):
        file = request.get_data() 
        angle_of_rotation = request.args.get('angle_of_rotation')
        page_number = request.args.get('page_number')
        base = request.args.get('isbase')

        if base == "True":
            return pdfbsf(file, angle_of_rotation, page_number)
        else:
            return pdf(file, angle_of_rotation, page_number)