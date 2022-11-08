from flask import jsonify, make_response, send_file
from PyPDF2 import PdfReader, PdfWriter
import io
import base64
import os


def pdf(file, angle_of_rotation, page_number):

    try:

        document = io.BytesIO(file)
        pdf_reader = PdfReader(document)
        pdf_page_numbers = len(pdf_reader.pages)
        page_number = int(page_number)
        angle_of_rotation = int(angle_of_rotation)
        file_name = f"abx.pdf"


        if angle_of_rotation not in [90,180,270]:
            return {"message":"Angle of Rotation degree must be one of these 90, 180, 270"}

        if page_number not in range(1, pdf_page_numbers+1):
            return {"message":f"input page number does not exists because this pdf only contain {pdf_page_numbers} pages"}


        writer = PdfWriter()
        return_data = io.BytesIO()


        for idxnum, page in enumerate(pdf_reader.pages):
            if idxnum == page_number-1:
                page.rotate_clockwise(angle_of_rotation)
            writer.add_page(page)


        with open(file_name, "wb") as pdf_out:
            writer.write(pdf_out)
        

        # This base64 online link file for streaming download
        # with open(file_name, 'rb') as fo:
        #     return_data.write(b"data:application/pdf;base64,")
        #     return_data.write(base64.b64encode(fo.read()))
        #     return_data.seek(0)  
        # os.remove(file_name)


        with open(file_name, 'rb') as fo:
            return_data.write(fo.read())
            return_data.seek(0)  
        os.remove(file_name)
    

        return send_file(return_data,as_attachment=True,mimetype='application/pdf',
                     attachment_filename='download_pdf.pdf')
 
    except Exception as e:
      return {"message":"Only pdf file are allowed"},400
    

