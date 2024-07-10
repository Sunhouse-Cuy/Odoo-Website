from odoo import http
from odoo.http import request
from odoo.exceptions import MissingError
import base64
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter


class Estates(http.Controller):

    @http.route('/estates', type='http', auth='public', website=True)
    def index(self, **post):
        return request.render('Estate.products', {})

    @http.route('/estates/entry', type='http', auth='public', website=True)
    def estate(self, **kw):

        image = kw.get('image')

        image_base64 = False
        if image and hasattr(image, 'read'):
            image_base64 = base64.b64encode(image.read())

        record = request.env['real.estate'].sudo().create({
            'name': kw.get('name'),
            'email': kw.get('email'),
            'expected_price': kw.get('expected_price'),
            'description': kw.get('description'),
            'postcode': kw.get('postcode'),
            'date_availability': kw.get('date_availability'),
            'bedrooms': kw.get('bedrooms'),
            'living_area': kw.get('living_area'),
            'facades': kw.get('facades'),
            'garage': kw.get('garage'),
            'garden': kw.get('garden'),
            'garden_area': kw.get('garden_area'),
            'garden_orientation': kw.get('garden_orientation'),
            'image': image_base64,
        })

        return request.redirect('/thank_you/%s' % record.id)

    @http.route('/thank_you/<int:estate_id>', type='http', auth='public', website=True)
    def thank_you(self, estate_id):
        return request.render('Estate.thank_you', {'estate_id': estate_id})

    @http.route('/estates/pdf/<int:estate_id>', type='http', auth='public', website=True)
    def estate_pdf(self, estate_id, **kwargs):
        try:
            pdf_report = request.env.ref('Estate.report_estate_detail')
            pdf_content, content_type = pdf_report.sudo()._render_qweb_pdf([estate_id])
            pdfhttpheaders = [
                ('Content-Type', 'application/pdf'),
                ('Content-Length', len(pdf_content)),
                ('Content-Disposition', f'attachment; filename="estate_report_{estate_id}.pdf"')
            ]
            return request.make_response(pdf_content, headers=pdfhttpheaders)
        except MissingError as e:
            return request.render('Estate.thank_you', {'error': str(e)})
        except Exception as e:
            return request.render('Estate.thank_you', {'error': 'An error occurred while generating the PDF.'})


@http.route('/estates/pdf_combined/<int:estate_id>', type='http', auth='user')
def download_combined_pdf(self, estate_id):
    estate = request.env['real.estate'].browse(estate_id)
    estates = [{'estate_pdf_file': estate.estate_pdf_file}]
    additional_pdf_base64 = estate.additional_pdf_base64  # Înlocuiește cu metoda de obținere a PDF-ului adițional

    combined_pdf_base64 = combine_pdfs(estates, additional_pdf_base64)

    response = request.make_response(base64.b64decode(combined_pdf_base64))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=combined_estate_pdf.pdf'
    return response
