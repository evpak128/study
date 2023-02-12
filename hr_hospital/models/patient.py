import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Patient(models.Model):
    _name = 'hr.hosp.patient'
    _description = 'Patient'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
    medical_card_number = fields.Char()

    doctor_ids = fields.Many2many(
        comodel_name='hr.hosp.doctor', )

    disease_ids = fields.Many2many(
        comodel_name='hr.hosp.disease', )
