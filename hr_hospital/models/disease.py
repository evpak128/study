from odoo import models, fields


class Disease(models.Model):
    _name = 'hr.hospital.disease'
    _description = 'Disease'

    name = fields.Char()
    category_id = fields.Many2one(comodel_name='hr.hospital.disease.category')
