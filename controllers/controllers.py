# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloDemo(http.Controller):
#     @http.route('/modulo_demo/modulo_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_demo/modulo_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_demo.listing', {
#             'root': '/modulo_demo/modulo_demo',
#             'objects': http.request.env['modulo_demo.modulo_demo'].search([]),
#         })

#     @http.route('/modulo_demo/modulo_demo/objects/<model("modulo_demo.modulo_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_demo.object', {
#             'object': obj
#         })

