# -*- coding: utf-8 -*-

from odoo import models, fields, api


class candidate(models.Model):
    _name = "election.candidate"
    _description = "An honest candidate for president"
    _order = 'total_votes desc'

    name = fields.Char()
    voter_ids = fields.One2many("election.voter", "vote", string="Voters")
    total_votes = fields.Integer(
        "Total votes", compute="_compute_total_votes", store=True
    )

    @api.depends('voter_ids')
    def _compute_total_votes(self):
        self.total_votes = len(self.voter_ids)
