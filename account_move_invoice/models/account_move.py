# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account_move_invoice(models.Model):
    _inherit='account.move'
    

    total_exchange_khr = fields.Monetary(compute = '_compute_total_khmer', string="Total Amount in Khmer", currency_field='khr_currency_id')
    total_exchange_thb = fields.Monetary(compute = '_compute_total_bat', string="Total Amount in THB", currency_field='thb_currency_id')
    rate_khr = fields.Float(string="Exchange Khmer")
    rate_thb = fields.Float(string="Exchange Thb")
    khr_currency_id = fields.Many2one('res.currency', compute = '_compute_total_khmer')
    thb_currency_id = fields.Many2one('res.currency', compute = '_compute_total_bat')

    @api.depends('amount_total')
    def _compute_total_khmer(self):
        for invoice in self:
            invoice.total_exchange_khr = invoice.amount_total * invoice.rate_khr 
            invoice.khr_currency_id = self.env['res.currency'].search([('id','=',66)])
    def _compute_total_bat(self):
        for i in self:
            i.total_exchange_thb = i.amount_total * i.rate_thb
            i.thb_currency_id = self.env['res.currency'].search([('id','=',137)])
      
        


