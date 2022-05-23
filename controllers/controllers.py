# -*- coding: utf-8 -*-
# from odoo import http


# class IntegradoraBex(http.Controller):
#     @http.route('/integradora_bex/integradora_bex', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/integradora_bex/integradora_bex/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('integradora_bex.listing', {
#             'root': '/integradora_bex/integradora_bex',
#             'objects': http.request.env['integradora_bex.integradora_bex'].search([]),
#         })

#     @http.route('/integradora_bex/integradora_bex/objects/<model("integradora_bex.integradora_bex"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('integradora_bex.object', {
#             'object': obj
#         })
