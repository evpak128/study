from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Diagnosis(models.Model):
    _name = 'hr.hospital.diagnosis'
    _description = 'Diagnosis'

    name = fields.Char(required=True)
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    disease_id = fields.Many2one(comodel_name='hr.hospital.disease')
    category_id = fields.Many2one(comodel_name='hr.hospital.disease.category')
    treatment = fields.Text()
    date_of_diagnosis = fields.Date()
    comment = fields.Text()

    @api.constrains('doctor_id', 'comment')
    def _constrains_check_intern_comment(self):
        if self.doctor_id.is_intern and not self.comment:
            raise ValidationError(_('Mentor comment needed.'))

    @api.constrains('disease_id', 'patient_id')
    def write_disease_history(self):
        for rec in self:
            if rec.disease_id:
                self.env['hr.hospital.disease.history'].create({
                    'name': f'{rec.name} {rec.disease_id.name}',
                    'patient_id': rec.patient_id.id,
                    'disease_id': rec.disease_id.id,
                    'date_of_diagnosis': rec.date_of_diagnosis,
                })
