from odoo.tests.common import TransactionCase
from .. import controllers

class TestController(TransactionCase):

 def setUp(self, *args, **kwargs):
    super(TestController, self).setUp(*args, **kwargs)
    self.election_controller = controllers.controllers.Election()
    self.election_controller.request = self

 def test_set_vote_validates_missing_params(self):
     resp = self.election_controller.set_vote(None, None)
     self.assertDictEqual(resp, {'error': 'Missing params'})

 def test_set_vote_validates_unexisting_candidate(self):
     resp = self.election_controller.set_vote(10000, 1)
     self.assertDictEqual(resp, {'error': 'Unexisting candidate 10000'})

 def test_set_vote_validates_unexisting_voter(self):
     resp = self.election_controller.set_vote(1, 10000)
     self.assertDictEqual(resp, {'error': 'Unexisting voter 10000'})

 def test_set_vote_creates_the_vote_relation(self):
     resp = self.election_controller.set_vote(1, 1)
     self.assertDictEqual(resp, {'sucess': True })

#  def test_set_vote_creates_the_vote_relation(self):
#      resp = self.election_controller.set_vote(http_req_emulator, 1, 1)
#      self.assertDictEqual(resp, {'success': True })