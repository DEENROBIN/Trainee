from odoo import models, fields

class StudentSection(models.Model):
    _name = 'dcl.stp.student.section'
    _description = 'Student Section'

    name = fields.Char(string='Section Name', required=True)
