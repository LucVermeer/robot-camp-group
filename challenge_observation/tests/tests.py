import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'utility', 'edutest'))
import edutest

class Test_Exercise_Values(edutest.TestCase):
    def test(self):
        self.io_pair(('00:01', 5, '1990-01-01', 3), 1524877357732680)
        self.io_pair(('00:02', 6, '1990-01-02', 4), 1626536109368864)
        self.io_pair(('00:03', 7, '1990-01-03', 5), 2643120828396360)
        # @StartHiddenCases
        self.io_pair(('00:00', 25, '2024-06-14', 75569), 15253863997110712450)
        self.io_pair(('00:10', 95, '2024-07-31', 38230), 6494032927059601638817769026026600)
        # @EndHiddenCases

class Test_Exercise(edutest.TestSuite):
    test_cases = [
        Test_Exercise_Values
    ]