from odoo import api, fields, models
import base64
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter


class RealEstate(models.Model):
    _name = "real.estate"
    _description = "Real estate"
    _inherit = 'res.config.settings'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    postcode = fields.Char(string='Postcode')
    date_availability = fields.Date(string='Date Availability')
    expected_price = fields.Float(string='Expected Price')
    selling_price = fields.Float(string='Selling Price')
    bedrooms = fields.Integer(string='Bedrooms')
    living_area = fields.Integer(string='Living Area')
    facades = fields.Integer(string='Facades')
    garage = fields.Boolean(string='Garage')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Integer(string='Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ], string='Garden Orientation')
    buyer = fields.Text(string='Buyer')
    salesperson = fields.Text(string='Salesperson')
    email = fields.Text(string='Email')
    image = fields.Binary(string='Image')
    estate_pdf_file = fields.Binary(string="Estate PDF File", help="PDF file attached from settings")


def combine_pdfs(estates, additional_pdf_base64):
    pdf_writer = PdfWriter()

    # Add each estate PDF to the combined PDF
    for estate in estates:
        estate_pdf_bytes = base64.b64decode(estate['estate_pdf_file'])
        pdf_reader = PdfReader(BytesIO(estate_pdf_bytes))
        pdf_writer.add_pages(pdf_reader.pages)

    # Add the additional PDF
    if additional_pdf_base64:
        additional_pdf_bytes = base64.b64decode(additional_pdf_base64)
        pdf_reader = PdfReader(BytesIO(additional_pdf_bytes))
        pdf_writer.add_pages(pdf_reader.pages)

    combined_pdf_bytes = BytesIO()
    pdf_writer.write(combined_pdf_bytes)
    combined_pdf_bytes.seek(0)

    return base64.b64encode(combined_pdf_bytes.read()).decode('utf-8')
