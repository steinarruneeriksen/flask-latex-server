from flask import Flask, request
from flask_restful import Resource, Api
from tex.tex_manager import TexManager
from flask import send_file
from flask import make_response
import json
app = Flask(__name__)
api = Api(app)


class PdfLatexStream(Resource):
    def post(self):
        dict=json.loads(request.data)
        print(dict)
        tex_file = dict['tex_file']
        pdf_file_in_bytes = TexManager.ceate_pdf(tex_file)
        response = make_response(pdf_file_in_bytes)
        response.headers.set('Content-Type', 'application/pdfapplication/pdf')
        return response

class PdfLatexDownload(Resource):
    def post(self):
        tex_file = request.data['tex_file']
        pdf_file_in_bytes = TexManager.ceate_pdf(tex_file)
        response = make_response(pdf_file_in_bytes)
        response.headers.set('Content-Type', 'application/pdfapplication/pdf')
        response.headers.set(
            'Content-Disposition', 'attachment', filename='file.pdf')
        return response

class PdfLatexEmailer(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(PdfLatexDownload, '/api/pdflatex/latex2pdf-download/')
api.add_resource(PdfLatexStream, '/api/pdflatex/latex2pdf-stream/')
api.add_resource(PdfLatexEmailer, '/api/pdflatex/latex2pdf-emailer/')

if __name__ == '__main__':
    app.run(debug=True)
