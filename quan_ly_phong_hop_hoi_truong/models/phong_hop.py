from odoo import models, fields

class PhongHop(models.Model):
    _name = 'phong_hop'
    _description = 'Phòng họp'

    ten_phong = fields.Char(string="Tên phòng", required=True)
    suc_chua = fields.Integer(string="Sức chứa")
    vi_tri = fields.Char(string="Vị trí")
    trang_thai = fields.Selection([
        ('trong', 'Trống'),
        ('dang_su_dung', 'Đang sử dụng')
    ], string="Trạng thái", default='trong')
    thiet_bi_ids = fields.One2many('thiet_bi', 'phong_hop_id', string="Thiết bị")
    lich_su_su_dung_ids = fields.One2many('lich_su_su_dung', 'phong_hop_id', string="Lịch sử sử dụng")
