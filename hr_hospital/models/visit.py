from odoo import models, fields
from odoo.exceptions import AccessError


class PatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Patient Visit'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    diagnosis_id = fields.Many2one(comodel_name='hr.hospital.diagnosis')
    date_of_visit = fields.Datetime()
    recommendation = fields.Text()
    research_ids = fields.Many2many(comodel_name='hr.hospital.research')
    doctor_schedule_ids = fields.Many2many(comodel_name='hr.hospital.doctor.schedule')
    active = fields.Boolean(default=True)

    def unlink(self):
        if self.diagnosis_id:
            raise AccessError("This visit has diagnosis and you can't delete it")
        return super(PatientVisit, self).unlink()

    def action_archive(self):
        if self.diagnosis_id:
            raise AccessError("This visit has diagnosis and you can't archive it")
        return super(PatientVisit, self).action_archive()
