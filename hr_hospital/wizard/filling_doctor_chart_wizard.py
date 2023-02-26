from datetime import timedelta
from odoo import _, fields, models


class FillingDoctorChartWizard(models.TransientModel):
    _name = 'hr.hospital.filling.doctor.chart.wizard'
    _description = 'Filling Doctor Chart'

    doctor_id = fields.Many2one(comodel_name='hr.hospital.doctor',
                                required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    start_time_pair = fields.Float(string='Start time')
    end_time_pair = fields.Float(string='End time')
    start_time_unpair = fields.Float(string='Start time')
    end_time_unpair = fields.Float(string='End time')

    def action_open_wizard(self):
        return {
            'name': _("Fill doctor's schedule"),
            'type': 'ir.actions.act.window',
            'view_mode': 'form',
            'res_model': 'hr.hospital.fill.doctor.chart.wizard',
            'target': 'new',
        }

    def action_fill_chart(self):
        self.ensure_one()
        today_day = self.start_date
        while today_day <= self.end_date:
            start_time = self.start_time_unpair
            end_time = self.end_time_unpair
            if today_day.day % 2 == 0:
                start_time = self.start_time_pair
                end_time = self.end_time_pair
            self.env['hr.hospital.doctor.schedule'].create(
                {
                    'doctor_id': self.doctor_id.id,
                    'start_date': today_day,
                    'start_time': start_time,
                    'end_time': end_time,
                })
            today_day = today_day + timedelta(days=1)
