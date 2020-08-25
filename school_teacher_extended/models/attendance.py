# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class DailyAttendance(models.Model):
    _inherit = 'daily.attendance'

    subject_id = fields.Many2one('subject.subject', 'Subject')

    @api.onchange("user_id")
    def onchange_user_id(self):
        standards = self.user_id.mapped('standard_ids')
        subjects = self.user_id.mapped('subject_id')
        return {'domain': {'standard_id': [(
            'id', 'in', standards.ids)], 'subject_id': [(
                'id', 'in', subjects.ids)], }}
