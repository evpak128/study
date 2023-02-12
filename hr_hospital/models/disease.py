import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Disease(models.Model):
    _name = 'hr.hosp.disease'
    _description = 'Disease'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
