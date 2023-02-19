from odoo import models, fields, api


class DiseaseType(models.Model):
    _name = 'hr.hospital.disease.type'
    _description = 'Disease Type'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(required=True)
    complete_name = fields.Char('Complete Name',
                                compute='_compute_complete_name',
                                store=True)
    parent_id = fields.Many2one('hr.hospital.disease.type',
                                'Parent Category',
                                index=True,
                                ondelete='cascade')
    child_id = fields.One2many('hr.hospital.disease.type',
                               'parent_id',
                               'Child Categories')
    parent_path = fields.Char(index=True)

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name
