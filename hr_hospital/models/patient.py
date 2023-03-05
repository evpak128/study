from datetime import date
from odoo import models, fields, api, _


class Patient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'
    _inherit = 'abstract.person'

    birthday = fields.Date(string='Date of Birth')
    age = fields.Integer(compute='_compute_age')
    passport_info = fields.Char()
    personal_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor')
    contact_person_id = fields.Many2one(
        comodel_name='hr.hospital.contact.person')
    personal_doctors_ids = fields.One2many(
        comodel_name='hr.hospital.personal.doctor.history',
        inverse_name='patient_id')
    disease_history_ids = fields.One2many(
        comodel_name='hr.hospital.disease.history',
        inverse_name='patient_id')
    status = fields.Selection(selection=[('easy', _('Easy')),
                                         ('medium', _('Medium')),
                                         ('hard', _('Hard'))])

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

    def analysis_history(self):
        self.ensure_one()

        return {
            'name': _('Analysis History'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr.hospital.analysis',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)]
        }

    def visit_history(self):
        self.ensure_one()

        return {
            'name': _('Visit History'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr.hospital.patient.visit',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)]
        }

    def diagnosis_history(self):
        self.ensure_one()

        return {
            'name': _('Diagnosis History'),
            'type': 'ir.actions.act_window',
            'res_model': 'hr.hospital.diagnosis',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)]
        }
