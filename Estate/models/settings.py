from odoo import api, fields, models, _


class EstateSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    note = fields.Char(string='Note')
    estate_pdf_file = fields.Binary(string="Estate PDF File", attachment=True)

    def set_values(self):
        super(EstateSettings, self).set_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        ICPSudo.set_param('Estate.note', self.note)
        ICPSudo.set_param('Estate.estate_pdf_file', self.estate_pdf_file)
        return True

    @api.model
    def get_values(self):
        res = super(EstateSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        note = ICPSudo.get_param('Estate.note')
        estate_pdf_file = ICPSudo.get_param('Estate.estate_pdf_file')
        res.update({
            'note': note,
            'estate_pdf_file': estate_pdf_file,
        })
        return res