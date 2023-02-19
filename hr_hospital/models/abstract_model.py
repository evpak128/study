from odoo import models, fields


class AbstractPerson(models.AbstractModel):
    _name = 'abstract.person'
    _description = 'Abstract Person'

    name = fields.Char()
    phone_number = fields.Char()
    email = fields.Char()
    gender = fields.Selection(selection=[('male', 'Male'),
                                         ('female', 'Female'),
                                         ('other', 'Other / Undefined')])
    photo = fields.Binary()
