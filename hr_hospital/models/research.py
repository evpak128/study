from odoo import models, fields


class Research(models.Model):
    _name = 'hr.hospital.research'
    _description = 'Research'

    name = fields.Char()
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    research_type = fields.Many2one(comodel_name='hr.hospital.research.type')
    example = fields.Many2one(comodel_name='hr.hospital.example')
    result = fields.Text()
