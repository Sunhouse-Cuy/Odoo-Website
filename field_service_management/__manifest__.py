{
    'name': 'Field Service Travel Orders',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage travel orders and associated expenses',
    'description': """
        This module allows field service companies to manage travel orders, associate customer invoices, and track expenses.
    """,
    'depends': ['base', 'fleet', 'account', 'hr_expense'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/travel_order_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
