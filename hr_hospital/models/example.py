from odoo import models, fields


class Example(models.Model):
    _name = 'hr.hospital.example'
    _description = 'Example'

    name = fields.Char()
