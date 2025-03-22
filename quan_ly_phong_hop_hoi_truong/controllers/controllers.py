# -*- coding: utf-8 -*-
# from odoo import http


# class QuanLyPhongHopHoiTruong(http.Controller):
#     @http.route('/quan_ly_phong_hop_hoi_truong/quan_ly_phong_hop_hoi_truong', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quan_ly_phong_hop_hoi_truong/quan_ly_phong_hop_hoi_truong/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quan_ly_phong_hop_hoi_truong.listing', {
#             'root': '/quan_ly_phong_hop_hoi_truong/quan_ly_phong_hop_hoi_truong',
#             'objects': http.request.env['quan_ly_phong_hop_hoi_truong.quan_ly_phong_hop_hoi_truong'].search([]),
#         })

#     @http.route('/quan_ly_phong_hop_hoi_truong/quan_ly_phong_hop_hoi_truong/objects/<model("quan_ly_phong_hop_hoi_truong.quan_ly_phong_hop_hoi_truong"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quan_ly_phong_hop_hoi_truong.object', {
#             'object': obj
#         })
