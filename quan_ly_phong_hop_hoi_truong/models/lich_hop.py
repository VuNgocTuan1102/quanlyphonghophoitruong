from odoo import models, fields, api

class LichHop(models.Model):
    _name = 'lich_hop'
    _description = 'Lịch họp'

    ten_cuoc_hop = fields.Char(string="Tên cuộc họp", required=True)
    phong_hop_id = fields.Many2one('phong_hop', string="Phòng họp", required=True)
    hoi_dong_id = fields.Many2one('hoi_dong', string="Hội đồng", required=True)
    thoi_gian_bat_dau = fields.Datetime(string="Thời gian bắt đầu", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc", required=True)
    nguoi_tham_gia_ids = fields.Many2many('res.users', string="Người tham gia")

    @api.onchange('phong_hop_id')
    def _kiem_tra_phong_trong(self):
        if self.phong_hop_id:
            self.phong_hop_id.trang_thai = 'dang_su_dung'
