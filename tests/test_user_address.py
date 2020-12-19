import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestUserAddress(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.useraddress = mm.user.address

    def test_read_telephone(self):
        self.assertEqual('Telephone', self.useraddress.telephone)

    def test_read_county(self):
        self.assertEqual('CountyState', self.useraddress.county)

    def test_read_city(self):
        self.assertEqual('Town', self.useraddress.city)

    def test_read_zipcode(self):
        self.assertEqual('PostalCode', self.useraddress.zipcode)

    def test_read_street(self):
        self.assertEqual('Street', self.useraddress.street)


if __name__ == '__main__':
    unittest.main()
