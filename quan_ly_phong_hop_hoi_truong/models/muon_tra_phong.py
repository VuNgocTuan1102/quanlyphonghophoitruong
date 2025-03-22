from odoo import models, fields, api

class MuonTraPhong(models.Model):
    _name = 'muon_tra_phong'
    _description = 'Đơn đăng ký mượn, trả phòng'

    phong_hop_id = fields.Many2one('phong_hop', string="Phòng họp", required=True)
    nguoi_muon_id = fields.Many2one('nguoi_muon', string="Người mượn", required=True)
    thoi_gian_muon = fields.Datetime(string="Thời gian mượn", required=True)
    thoi_gian_tra = fields.Datetime(string="Thời gian trả", required=True)
    trang_thai = fields.Selection([
        ('dang_muon', 'Đang mượn'),
        ('da_tra', 'Đã trả')
    ], string="Trạng thái", default='dang_muon')
