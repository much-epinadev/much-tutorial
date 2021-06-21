# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class voter(models.Model):
    _name = "election.voter"
    _description = _("An innocent voter")

    name = fields.Char()
    vote = fields.Many2one("election.candidate", string=_("Vote"))
