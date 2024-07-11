from odoo import models, fields
from odoo.tools.translate import _



class AccountMove(models.Model):
    _inherit = 'account.move'


    travel_order_id = fields.Many2one('account.move', string='Travel Order')
    date_invoice = fields.Date(string='Invoice Date')

