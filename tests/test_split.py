import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestSplit(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.splits = mm.transactions[0].splits
        self.split0 = self.splits[0]

    def test_read_splits_count(self):
        self.assertEqual(2, len(self.splits))

    def test_read_payee(self):
        self.assertEqual('', self.split0.payee)

    def test_read_memo(self):
        self.assertEqual('', self.split0.memo)

    def test_read_shares(self):
        self.assertEqual('42/1', self.split0.shares)

    def test_read_number(self):
        self.assertEqual('', self.split0.number)

    def test_read_action(self):
        self.assertEqual('', self.split0.action)

    def test_read_price(self):
        self.assertEqual('1/1', self.split0.price)

    def test_read_account(self):
        self.assertEqual('A000001', self.split0.account)

    def test_read_reconcileflag(self):
        self.assertEqual('0', self.split0.reconcileFlag)

    def test_read_bankid(self):
        self.assertEqual('', self.split0.bankId)

    def test_read_value(self):
        self.assertEqual('42/1', self.split0.value)

    def test_read_reconciledate(self):
        self.assertEqual('', self.split0.reconcileDate)

    def test_read_id(self):
        self.assertEqual('S0001', self.split0.id)


if __name__ == '__main__':
    unittest.main()
