from odoo import models, fields, api


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char()
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease')
    treatment = fields.Text()
    date_of_diagnosis = fields.Datetime()
    comment = fields.Text()
    doctor_is_intern = fields.Boolean(default=False)
    research_ids = fields.Many2many(comodel_name='hr.hospital.research')

    @api.onchange('doctor_id')
    def onchange_doctor(self):
        for rec in self:
            if rec.doctor_id.is_intern:
                rec.doctor_is_intern = True
            else:
                rec.doctor_is_intern = False
