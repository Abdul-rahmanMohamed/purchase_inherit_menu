# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = "Odoo dev task"
    _rec_name = 'req_name'
    req_name = fields.Char(string="Request name", required=True)
    req_by = fields.Many2one('res.users', string="Requested by", required=True, default=lambda self: self.env.user)
    start_date = fields.Date(default=fields.Date.today, string="Start date")
    end_date = fields.Date(string="End date")
    reject_reason = fields.Text(string="Rejection Reason")
    order_lines = fields.One2many('order.lines', 'order_id', string="ORDERLINES")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_be_approve', 'To Be Approve'),
        ('approved', 'Approved'),
        ('reject', 'Reject'),
        ('cancel', 'Cancel')],
        string='Status', default='draft', readonly=True, copy=False, tracking=True)
    email_id = fields.Text(string="Email", required=True)
    amount_total = fields.Float(string='Total', store=True, readonly=True)

    def submit_to_approve(self):
        self.state = 'to_be_approve'

    def cancel_req(self):
        self.state = 'cancel'

    def approve_req(self):
        template_id = self.env.ref('purchase_menu.report_template_mail').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send="group_manager_purchase_menu")
        self.state = 'approved'

    def reset_to_draft(self):
        self.state = 'draft'


class OrderLinesRequest(models.Model):
    _name = 'order.lines'
    _description = 'Order Lines '

    product_id = fields.Many2one('product.product', string="Product_ID", required=True)
    description = fields.Char(string="Description", related='product_id.name')
    quantity = fields.Float(string="Quantity", default=1.0)
    cost_price = fields.Float(String="Cost")
    total = fields.Float(String="Total", compute='_compute_total')
    order_id = fields.Many2one('purchase.request', string="Order.No")

    def _compute_total(self):
        for rec in self:
            rec.total = rec.cost_price * rec.quantity
