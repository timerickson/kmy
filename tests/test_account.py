import unittest
from kmy.kmy import Kmy

file_name = 'Test.kmy'


class TestAccount(unittest.TestCase):
    def setUp(self):
        mm = Kmy.from_kmy_file(file_name)
        self.accounts = mm.accounts
        self.account0 = self.accounts[0]

    def test_read_accounts_count(self):
        self.assertEqual(11, len(self.accounts))

    def test_read_number(self):
        self.assertEqual('', self.account0.number)

    def test_read_lastmodified(self):
        self.assertEqual('', self.account0.lastModified)

    def test_read_institution(self):
        self.assertEqual('', self.account0.institution)

    def test_read_name(self):
        self.assertEqual('Asset', self.account0.name)

    def test_read_currency(self):
        self.assertEqual('USD', self.account0.currency)

    def test_read_parentaccount(self):
        self.assertEqual('', self.account0.parentAccount)

    def test_read_lastreconciled(self):
        self.assertEqual('', self.account0.lastReconciled)

    def test_read_description(self):
        self.assertEqual('', self.account0.description)

    def test_read_type(self):
        self.assertEqual('9', self.account0.type)

    def test_read_opened(self):
        self.assertEqual('', self.account0.opened)

    def test_read_id(self):
        self.assertEqual('AStd::Asset', self.account0.id)

    def test_read_subaccounts(self):
        self.assertEqual(1, len(self.account0.subAccounts))

    def test_read_subaccount_id(self):
        self.assertEqual('A000001', self.account0.subAccounts[0].id)


if __name__ == '__main__':
    unittest.main()
