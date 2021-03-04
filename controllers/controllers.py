# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseInherit(http.Controller):
#     @http.route('/purchase_menu/purchase_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_menu/purchase_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_menu.listing', {
#             'root': '/purchase_menu/purchase_menu',
#             'objects': http.request.env['purchase_menu.purchase_menu'].search([]),
#         })

#     @http.route('/purchase_menu/purchase_menu/objects/<model("purchase_menu.purchase_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_menu.object', {
#             'object': obj
#         })
