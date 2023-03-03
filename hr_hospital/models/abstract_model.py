from odoo import models, fields, _


class AbstractPerson(models.AbstractModel):
    _name = 'abstract.person'
    _description = 'Abstract Person'

    name = fields.Char()
    phone_number = fields.Char()
    email = fields.Char()
    gender = fields.Selection(selection=[('male', _('Male')),
                                         ('female', _('Female')),
                                         ('other', _('Other / Undefined'))])
    photo = fields.Binary()
