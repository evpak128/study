from datetime import date
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'
    _inherit = 'abstract.person'

    birthday = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')
    passport_info = fields.Char()
    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor')
    disease_ids = fields.Many2many(
        comodel_name='hr.hospital.disease')
    contact_person_id = fields.Many2one(
        comodel_name='hr.hospital.contact.person')

    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                rec.age = (date.today() - rec.birthday).days // 365
            else:
                rec.age = 0

    @api.constrains('personal_doctor_id')
    def write_date_history(self):
        for rec in self:
            if rec.personal_doctor_id:
                self.env['hr.hospital.personal.doctor.history'].create({
                    'name': f'{rec.name} {rec.personal_doctor_id.name}',
                    'patient_id': rec.id,
                    'personal_doctor_id': rec.personal_doctor_id.id,
                    'appointment_date': fields.Date.today()
                })
