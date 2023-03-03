from odoo import models, fields


class Analysis(models.Model):
    _name = 'hr.hospital.analysis'
    _description = 'Analysis'

    analysis_name = fields.Char()
    analysis_type = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    phone_number = fields.Char()
    date_of_analysis = fields.Date()
