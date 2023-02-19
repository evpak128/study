from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'
    _inherit = 'abstract.person'

    specialty = fields.Char()
    is_intern = fields.Boolean(default=False)
    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                domain="[('is_intern', '=', False)]")
