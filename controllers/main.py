from odoo import http
from odoo.http import request

class ElectroWordFrontend(http.Controller):

    @http.route('/products_page', type='http', auth='public', website=True)
    def products_page(self):
        """ Muestra una página con productos en el sitio web """
        products = request.env['product.template'].sudo().search([])
        return request.render('electroword_api.products_template', {'products': products})

    @http.route('/customers_page', type='http', auth='public', website=True)
    def customers_page(self):
        """ Muestra una página con clientes en el sitio web """
        customers = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
        return request.render('electroword_api.customers_template', {'customers': customers})