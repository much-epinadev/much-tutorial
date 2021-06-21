# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import base64
import io


class DataImport(models.TransientModel):
    _name = "election.data.import"
    _description = "Data Import"

    csv_file = fields.Binary(string=_("CSV Election file"))

    def _get_voter_object(self, voter_name):
        voter_model = self.env["election.voter"]
        voter = voter_model.search([("name", "=", voter_name)])

        return voter if voter.exists() else voter_model.create({"name": voter_name})

    def import_data(self):
        data_content = []
        try:
            inputx = io.BytesIO()
            inputx.write(base64.decodebytes(self.csv_file))
            decoded_data = inputx.getvalue().decode()
            # Remove the csv headers (position 0) from the decoded data
            data_content = decoded_data.split("\n")[1:]
        except TypeError as e:
            raise ValidationError(u"ERROR: {}".format(e))

        if len(data_content) > 0:
            for line in data_content:
                if "," in line:
                    voter_name, candidate_name = line.split(",")
                    voter = self._get_voter_object(voter_name)
                    candidate = self.env["election.candidate"].search(
                        [("name", "=", candidate_name)]
                    )
                    if candidate.exists():
                        voter.vote = candidate
                    else:
                        raise exceptions.UserError(
                            f'Candidate: {candidate_name} not found!'
                        )
