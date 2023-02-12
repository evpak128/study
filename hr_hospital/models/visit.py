import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class PatientVisit(models.Model):
    _name = 'hr.hosp.patient.visit'
    _description = 'Patient Visit'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )

    patient_ids = fields.Many2many(
        comodel_name='hr.hosp.patient', )
