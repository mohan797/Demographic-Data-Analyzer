import unittest
from demographic_data_analyzer import demographic_data_analyzer

class TestDemographicAnalyzer(unittest.TestCase):
    def setUp(self):
        self.result = demographic_data_analyzer()

    def test_race_count(self):
        self.assertTrue('White' in self.result['race_count'].index)

    def test_average_age_men(self):
        self.assertIsInstance(self.result['average_age_men'], float)

    def test_percentage_bachelors(self):
        self.assertGreater(self.result['percentage_bachelors'], 15.0)

    def test_top_IN_occupation(self):
        self.assertIsInstance(self.result['top_IN_occupation'], str)

if _name_ == "_main_":
    unittest.main()
