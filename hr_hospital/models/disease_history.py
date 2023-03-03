from odoo import models, fields


class DiseaseHistory(models.Model):
    _name = 'hr.hospital.disease.history'
    _description = 'Disease History'

    name = fields.Char()
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease')
    date_of_diagnosis = fields.Date()
