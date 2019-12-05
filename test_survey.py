import unittest
from survey import AnonymousSurvey

class TestAnomyousSurvey(unittest.TestCase):

    def setUp(self):
        question = "what language did you first learn to speak"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english','spanish','canesdlish']


    def test_store_singele_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)



unittest.main()