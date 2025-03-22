from odoo import models, fields

class NguoiMuon(models.Model):
    _name = 'nguoi_muon'
    _description = 'Người mượn'

    ten_nguoi_muon = fields.Char(string="Tên người mượn", required=True)
    email = fields.Char(string="Email")
    so_dien_thoai = fields.Char(string="Số điện thoại")
    muon_tra_phong_ids = fields.One2many('muon_tra_phong', 'nguoi_muon_id', string="Đơn mượn phòng")

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.ten_nguoi_muon} ({record.email})" if record.email else record.ten_nguoi_muon
            result.append((record.id, name))
        return result
