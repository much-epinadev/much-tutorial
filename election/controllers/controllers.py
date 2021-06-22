# -*- coding: utf-8 -*-
from odoo import http, _
import json

class Election(http.Controller):

    request = http.request

    def set_vote(self, candidate_id, voter_id):
        if candidate_id and voter_id:
            candidate = self.request.env["election.candidate"].sudo().browse(int(candidate_id))
            voter = self.request.env["election.voter"].sudo().browse(int(voter_id))

            if not voter.exists():
                return {"error": f"Unexisting voter {voter.id}"}

            if not candidate.exists():
                return {"error": f"Unexisting candidate {candidate.id}"}

            voter.vote = candidate
            return {"sucess": True}
        return { "error": "Missing params" }

    # ---------- Endpoints handlers ------------------
    @http.route("/election/", auth="public")
    def index(self, **kw):
        return "Hello, world"

    @http.route("/election/get_leading_candidate", auth="none")
    def get_leading_candidate(self):
        # Candidate with the highest amount of votes
        candidates = self.request.env["election.candidate"].sudo().search([])
        leading = None

        if len(candidates) > 0:
            leading = candidates[0]

            for candidate in candidates:
                if leading.total_votes < candidate.total_votes:
                    leading = candidate
            return json.dumps({"name": leading.name, "votes": leading.total_votes})
        return json.dumps({"error": "No candidate registered"})


    @http.route("/election/vote", auth="none", type="http")
    def set_vote_via_http(self, candidate_id=None, voter_id=None):
        response = self.set_vote(candidate_id, voter_id)

        return json.dumps(response)

    @http.route("/election/vote/json", auth="none", methods=["POST"], type="json")
    def set_vote_via_json(self):
        return self.set_vote(
            self.request.jsonrequest.get("candidate_id"),
            self.request.jsonrequest.get("voter_id"),
        )
