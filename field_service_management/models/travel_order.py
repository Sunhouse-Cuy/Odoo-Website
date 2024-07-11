from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'
    _description = 'Travel Order'

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle', required=True)
    invoice_ids = fields.One2many('account.move', 'travel_order_id', string='Invoices')
    receipt_ids = fields.One2many('expense.receipt', 'travel_order_id', string='Receipts')
    technician_ids = fields.Many2many('res.partner', string='Technicians', domain="[('is_technician','=',True)]")
    number = fields.Char(string='Number', required=True, copy=False, readonly=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):

        if vals.get('number', _('New')) == _('New'):
            vals['number'] = self.env['ir.sequence'].next_by_code('account.move.travel.order.invoice') or _('New')
        res = super(AccountMove, self).create(vals)
        return res