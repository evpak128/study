from odoo import fields, models


class DiseaseReport(models.TransientModel):
    _name = 'disease.report.wizard'
    _description = 'Disease Report'

    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    def action_print_disease_report(self):
        self.ensure_one()
        domain_report = [
            ('date_of_diagnosis', '>=', self.start_date),
            ('date_of_diagnosis', '<=', self.end_date),
        ]
        diagnosis_report = self.env['hr.hospital.diagnosis'].search(domain_report)
        report_vals = []
        for rec in diagnosis_report.mapped('disease_id'):
            filter_diagnosis = diagnosis_report.filtered(
                lambda r: r.disease_id == rec)
            list_diagnosis = []
            for diagnosis in filter_diagnosis:
                list_diagnosis.append(diagnosis.name)

            report_vals.append({
                'disease': rec.name,
                'count': len(filter_diagnosis),
            })

        actions = {
            "name": "Disease Report",
            "view_mode": "form",  # tree
            "view_id": self.env.ref('hr_hospital.disease_report_count_wizard_view_form').id,
            "res_model": "disease.report.count.wizard",
            "type": "ir.actions.act_window",
            "context": {"data": report_vals},
            "target": "new",
            # "domain": [('id', 'in', lines.ids)]
        }

        return actions
