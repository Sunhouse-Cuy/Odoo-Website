{
    'name': 'Weight Calculator',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Module to calculate weight of an object based on material and dimensions',
    'description': 'Calculate weight based on material (steel or aluminum), length, width, and thickness',
    'author': 'Your Name',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/weight_calculator_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
