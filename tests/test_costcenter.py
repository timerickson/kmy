import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestCostCenter(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.costCenters = mm.costCenters

    def test_read_costcenters_count(self):
        self.assertEqual(0, len(self.costCenters))


if __name__ == '__main__':
    unittest.main()
