from odoo import models, fields

class HoiDong(models.Model):
    _name = 'hoi_dong'
    _description = 'Hội đồng họp'

    ten_hoi_dong = fields.Char(string="Tên hội đồng", required=True)
    thanh_vien_ids = fields.Many2many('res.users', string="Thành viên")
