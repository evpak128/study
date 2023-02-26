from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class DiseaseType(models.Model):
    _name = 'hr.hospital.disease.category'
    _description = 'Disease Category'
    _parent_name = "parent_id"
    _parent_store = True
    _rec_name = 'complete_name'
    _order = 'complete_name'

    name = fields.Char(index=True, required=True)
    complete_name = fields.Char(
        compute='_compute_complete_name',
        recursive=True,
        store=True)
    parent_id = fields.Many2one(
        comodel_name='hr.hospital.disease.category',
        string='Parent Category',
        index=True,
        ondelete='cascade')
    child_id = fields.One2many(
        comodel_name='hr.hospital.disease.category',
        inverse_name='parent_id',
        string='Child Categories')
    parent_path = fields.Char(index=True)
    disease_count = fields.Integer(compute='_compute_disease_count')

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for category in self:
            if category.parent_id:
                category.complete_name = '%s / %s' % (
                    category.parent_id.complete_name, category.name)
            else:
                category.complete_name = category.name

    def _compute_disease_count(self):
        for obj in self:
            obj.disease_count = self.env[
                'hr.hospital.disease'].search_count([
                ('category_id', 'child_of', obj.id),

            ])

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursion categories.'))
