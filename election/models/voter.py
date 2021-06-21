# -*- coding: utf-8 -*-

from odoo import models, fields, api

class voter(models.Model):
    _name = "election.voter"
    _description = "An innocent voter"

    name = fields.Char()
    vote = fields.Many2one("election.candidate", string="Vote")
