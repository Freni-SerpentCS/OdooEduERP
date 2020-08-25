# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class SchoolTeacher(models.Model):
    _inherit = 'school.teacher'

    standard_ids = fields.Many2many('school.standard', 'std_teacher_rel',
                                    'teacher_id', 'std_id',
                                    'Responsibility of Academic Classes')
