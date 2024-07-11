from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Weight Calculator'

    material = fields.Selection([
        ('steel', 'Steel'),
        ('aluminum', 'Aluminum')
    ], string='Material', required=True)
    length = fields.Float(string='Length (cm)', required=True)
    width = fields.Float(string='Width (cm)', required=True)
    thickness = fields.Float(string='Thickness (cm)', required=True)
    density = fields.Float(string='Density (g/cm³)', compute='_compute_density', store=True)
    weight = fields.Float(string='Weight (g)', compute='_compute_weight', store=True)

    @api.depends('material')
    def _compute_density(self):
        for record in self:
            if record.material == 'steel':
                record.density = 7.85  # g/cm³ for steel
            elif record.material == 'aluminum':
                record.density = 2.70  # g/cm³ for aluminum

    @api.depends('length', 'width', 'thickness', 'density')
    def _compute_weight(self):
        for record in self:
            volume = record.length * record.width * record.thickness  # cm³
            record.weight = volume * record.density  # g
