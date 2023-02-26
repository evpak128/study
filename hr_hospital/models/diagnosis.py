from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease')
    treatment = fields.Text()
    date_of_diagnosis = fields.Date()
    comment = fields.Text()

    @api.constrains('doctor_id', 'comment')
    def _constrains_check_intern_comment(self):
        if self.doctor_id.is_intern and not self.comment:
            raise ValidationError(_('Mentor comment needed.'))
