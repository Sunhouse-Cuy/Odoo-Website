from odoo import models, fields

class ExpenseReceipt(models.Model):
    _name = 'expense.receipt'
    _description = 'Expense Receipt'

    name = fields.Char(string='Receipt Reference', required=True)
    date = fields.Date(string='Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    travel_order_id = fields.Many2one('travel.order', string='Travel Order', required=True)
