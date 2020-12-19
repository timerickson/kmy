import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestPayeeAddress(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.address = mm.payees[0].address

    def test_read_telephone(self):
        self.assertEqual('+1 312 123 4567', self.address.telephone)

    def test_read_state(self):
        self.assertEqual('WH', self.address.state)

    def test_read_city(self):
        self.assertEqual('Whoville', self.address.city)

    def test_read_street(self):
        self.assertEqual("123 Street\n42 Something", self.address.street)

    def test_read_postcode(self):
        self.assertEqual('WHO 123', self.address.postCode)


if __name__ == '__main__':
    unittest.main()
