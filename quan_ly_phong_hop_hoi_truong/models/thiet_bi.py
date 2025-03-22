from odoo import models, fields

class ThietBi(models.Model):
    _name = 'thiet_bi'
    _description = 'Thiết bị trong phòng'

    ten_thiet_bi = fields.Char(string="Tên thiết bị", required=True)
    phong_hop_id = fields.Many2one('phong_hop', string="Phòng họp", required=True)
    trang_thai = fields.Selection([
        ('tot', 'Tốt'),
        ('hong', 'Hỏng')
    ], string="Trạng thái", default='tot')
