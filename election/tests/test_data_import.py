from odoo.tests.common import TransactionCase

class TestDataImport(TransactionCase):

 def setUp(self, *args, **kwargs):
    super(TestDataImport, self).setUp(*args, **kwargs)
    self.data_import = self.env['election.data.import'].create({})
    candidate = self.env['election.candidate'].create({ 'name': 'Test Candidate 1' })
    self.test_voter = self.env['election.voter'].create({ 'name': 'Test Voter 1' })
    self.test_voter.vote = candidate

 def test_get_voter(self):
    """Should obtain the voter if this exists"""
    voter = self.data_import._get_voter_object('Test Voter 1')
    self.assertEqual(voter.vote.name, 'Test Candidate 1', 'Test Voter should exists')

 def test_get_new_voter(self):
    """Should create the voter if this does not exists"""
    voter = self.data_import._get_voter_object('Test Voter 2')
    self.assertEqual(voter.vote.name, False, 'Test Voter should be created')
