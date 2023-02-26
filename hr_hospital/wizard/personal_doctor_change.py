from odoo import fields, models


class PersonalDoctorChange(models.TransientModel):
    _name = "personal.doctor.change"
    _description = "Re-change for new personal doctor"

    personal_doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')

    def personal_doctor_change(self):
        patient_list = self.env['hr.hospital.patient'].browse(
            self.env.context.get('active_ids')
        )
        for patient in patient_list:
            patient.personal_doctor_id = self.personal_doctor_id
