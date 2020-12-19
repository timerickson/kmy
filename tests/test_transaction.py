import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestTransaction(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.transactions = mm.transactions
        self.transaction0 = self.transactions[0]

    def test_read_accounts_count(self):
        self.assertEqual(5, len(self.transactions))

    def test_read_postdate(self):
        self.assertEqual('2020-01-01', self.transaction0.postDate)

    def test_read_memo(self):
        self.assertEqual('', self.transaction0.memo)

    def test_read_commodity(self):
        self.assertEqual('USD', self.transaction0.commodity)

    def test_read_entrydate(self):
        self.assertEqual('2020-12-13', self.transaction0.entryDate)

    def test_read_id(self):
        self.assertEqual('T000000000000000001', self.transaction0.id)

    def test_read_splits(self):
        self.assertEqual(2, len(self.transaction0.splits))


if __name__ == '__main__':
    unittest.main()
