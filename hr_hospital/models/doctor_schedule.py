from odoo import models, fields, api, _
from odoo.exceptions import AccessError


class DoctorSchedule(models.Model):
    _name = 'hr.hospital.doctor.schedule'
    _description = 'Doctor Schedule'
    _rec_name = 'doctor_id'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor')
    start_date = fields.Date()
    end_date = fields.Date()
    start_time = fields.Float()
    end_time = fields.Float()
    is_visit_done = fields.Boolean()

    @api.constrains('start_date', 'end_date')
    def check_schedule(self):
        for rec in self:
            if not rec.start_date or not rec.end_date:
                continue
            for schedule in self.env['hr.hospital.doctor.schedule'].search([('doctor_id', '=', rec.doctor_id.id)]):
                if rec.id == schedule.id:
                    continue
                if rec.start_date < schedule.end_date and rec.end_date < schedule.end_date:
                    raise AccessError(_('Time is busy'))
                if rec.start_date < schedule.start_date and rec.end_date < schedule.start_date:
                    raise AccessError(_('Time is busy'))
                if rec.start_date == schedule.start_date and rec.end_date == schedule.end_date:
                    raise AccessError(_('Time is busy'))
