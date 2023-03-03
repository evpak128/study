from odoo import models, fields


class PersonalDoctorHistory(models.Model):
    _name = 'hr.hospital.personal.doctor.history'
    _description = 'Personal Doctor History'

    name = fields.Char()
    personal_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    appointment_date = fields.Date()
