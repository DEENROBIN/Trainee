from odoo import models, fields

class StudentInstitute(models.Model):
    _name = 'dcl.stp.student.institute'
    _description = 'Student Institute'

    name = fields.Char(string='Institute Name', required=True)
