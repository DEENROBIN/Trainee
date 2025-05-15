from odoo import models, fields

class StudentClass(models.Model):
    _name = 'dcl.stp.student.class'
    _description = 'Student Class'

    name = fields.Char(string='Class Name', required=True)
