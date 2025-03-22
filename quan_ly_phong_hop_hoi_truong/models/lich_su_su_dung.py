from odoo import models, fields

class LichSuSuDung(models.Model):
    _name = 'lich_su_su_dung'
    _description = 'Lịch sử sử dụng phòng'

    phong_hop_id = fields.Many2one('phong_hop', string="Phòng họp", required=True)
    thoi_gian_bat_dau = fields.Datetime(string="Thời gian bắt đầu", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc", required=True)
    nguoi_su_dung_id = fields.Many2one('nguoi_muon', string="Người sử dụng", required=True)
