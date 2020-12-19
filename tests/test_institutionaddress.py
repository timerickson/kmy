import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestInstitutionAddress(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.address = mm.institutions[0].address

    def test_read_telephone(self):
        self.assertEqual('', self.address.telephone)

    def test_read_city(self):
        self.assertEqual('', self.address.city)

    def test_read_zip(self):
        self.assertEqual('', self.address.zip)

    def test_read_street(self):
        self.assertEqual('', self.address.street)


if __name__ == '__main__':
    unittest.main()
