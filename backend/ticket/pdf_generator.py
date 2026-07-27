"""
PDF Generator
Version 1
"""


class PDFGenerator:

    def generate(self, ticket):

        return {

            "pdf_name": f'{ticket["ticket_number"]}.pdf',

            "status": "Generated"

        }
