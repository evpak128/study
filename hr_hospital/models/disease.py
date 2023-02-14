import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Disease(models.Model):
    _name = 'hr.hosp.disease'  # краще не скорочувати назви "hr.hospital.disease"
    _description = 'Disease'  # Бажано додавати більш розгорнутий опис

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
