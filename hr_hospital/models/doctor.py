from odoo import models, fields


class Doctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'
    _inherit = 'abstract.person'

    specialty = fields.Char()
    is_intern = fields.Boolean(default=False)
    mentor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                domain=[('is_intern', '=', False)])
    intern_ids = fields.One2many(comodel_name='hr.hospital.doctor',
                                 inverse_name='mentor_id')
    personal_patient_ids = fields.One2many(comodel_name='hr.hospital.patient',
                                           inverse_name='personal_doctor_id')
    visit_ids = fields.One2many(comodel_name='hr.hospital.patient.visit',
                                inverse_name='doctor_id')
