# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class RejectRequestWizard(models.TransientModel):
    _name = 'reject.request.wizard'
    _description = 'rejection'
    reason = fields.Text(required=True)

    def action_confirm(self):
        active_id = self.env.context.get("active_id")
        pr = self.env['purchase.request'].browse(active_id)
        pr.write({
            'reject_reason': self.reason,
            'state': 'reject',
        })
