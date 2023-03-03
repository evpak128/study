from odoo import fields, models


class DiseaseReportCount(models.TransientModel):
    _name = 'disease.report.count.wizard'
    _description = 'Disease Report Count'

    def get_disease_report(self):
        html_table = '<table class="table table-bordered"><tbody>'
        html_table += '<tr><th>Disease</th><th>Count</th>'
        disease_data = self.env.context.get("data")
        for user in disease_data:
            html_table += f'<tr><td>{user["disease"]}</td><td>{user["count"]}</td>'

        html_table += '</tbody></table>'
        return html_table

    result_disease_report = fields.Html(
        string="Result",
        default=get_disease_report)
