from odoo import models, fields, api

class DatPhong(models.Model):
    _name = 'dat_phong'
    _description = 'Đặt phòng'

    phong_hop_id = fields.Many2one('phong_hop', string="Phòng họp", required=True)
    nguoi_dat_id = fields.Many2one('nguoi_muon', string="Người đặt", required=True)
    thoi_gian_bat_dau = fields.Datetime(string="Thời gian bắt đầu", required=True)
    thoi_gian_ket_thuc = fields.Datetime(string="Thời gian kết thúc", required=True)
    trang_thai = fields.Selection([
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('da_xac_nhan', 'Đã xác nhận'),
        ('da_huy', 'Đã hủy')
    ], string="Trạng thái", default='cho_xac_nhan')

    @api.onchange('phong_hop_id')
    def _kiem_tra_phong_trong(self):
        if self.phong_hop_id:
            self.phong_hop_id.trang_thai = 'dang_su_dung'
