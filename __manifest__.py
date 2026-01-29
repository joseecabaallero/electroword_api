{
    'name': 'ElectroWord API',
    'version': '1.0',
    'summary': 'API REST para obtener productos y clientes en Odoo',
    'author': 'José David,
    'category': 'API',
    'depends': ['base', 'sale', 'product', 'website'],
    'data': [
        'views/customers_template.xml', # Vista de clientes
        'views/products_template.xml', # Vista de productos
    ],
    'icon': '/electroword_api/static/description/icon59.png',
    'installable': True,
    'application': False,
}