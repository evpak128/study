from odoo import models, fields, _, api
from odoo.exceptions import AccessError, UserError, ValidationError


class PatientVisit(models.Model):
    _name = 'hr.hospital.patient.visit'
    _description = 'Patient Visit'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(comodel_name='hr.hospital.patient')
    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    diagnosis_id = fields.Many2one(comodel_name='hr.hospital.diagnosis')
    date_of_visit = fields.Datetime(string="Data/Time visit",
                                    default=fields.Datetime.now)
    recommendation = fields.Text()
    active = fields.Boolean(default=True)
    is_visit_done = fields.Boolean(string='Visit done', default=False)

    def unlink(self):
        if self.diagnosis_id:
            raise AccessError(_("This visit has diagnosis and you can't delete it"))
        return super(PatientVisit, self).unlink()

    def action_archive(self):
        if self.diagnosis_id:
            raise AccessError(_("This visit has diagnosis and you can't archive it"))
        return super(PatientVisit, self).action_archive()

    def write(self, vals):
        if 'date_of_visit' in vals:
            date_of_visit_val = vals['date_of_visit']
            for rec in self:
                if rec.is_visit_done and date_of_visit_val != rec.date_of_visit:
                    raise UserError(_("You can't change time"))
        if 'doctor_id' in vals:
            doctor_id_val = vals['doctor_id']
            for rec in self:
                if rec.is_visit_done and doctor_id_val != rec.doctor_id.id:
                    raise UserError(_("You can't change doc"))
        return super(PatientVisit, self).write(vals)

    @api.constrains('date_of_visit')
    def _constrains_check_visit_time(self):
        visit_list = self.env['hr.hospital.patient.visit'].search([])
        for rec in self:
            for visit in visit_list:
                if rec.id == visit.id:
                    continue
                if rec.date_of_visit == visit.date_of_visit:
                    raise ValidationError(_('Record already busy'))
