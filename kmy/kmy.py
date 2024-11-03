import gzip
import xml.etree.ElementTree as elementTree
from typing import Dict
from typing import List

from .account import Account
from .costcenter import CostCenter
from .fileinfo import FileInfo
from .institution import Institution
from .pairs import pairs_dict_from_xml
from .payee import Payee
from .tag import Tag
from .transaction import Transaction
from .user import User


class Kmy:
    def __init__(self):
        self.fileInfo: FileInfo = FileInfo()
        self.user: User = User()
        self.institutions: List[Institution] = []
        self.payees: List[Payee] = []
        self.costCenters: List[CostCenter] = []
        self.tags: List[Tag] = []
        self.accounts: List[Account] = []
        self.transactions: List[Transaction] = []
        self.keyValuePairs: Dict[str, str] = {}

    def __repr__(self):
        return f"{self.__class__.__name__}(fileInfo='{self.fileInfo}', user={self.user})"

    @classmethod
    def from_xml(cls, node):
        kmy: Kmy = cls()
        kmy.init_from_xml(node)
        return kmy

    def init_from_xml(self, node):
        self.fileInfo = FileInfo.from_xml(node.find('FILEINFO'))
        self.user = User.from_xml(node.find('USER'))
        institution_nodes = node.find('INSTITUTIONS')
        for institution_node in institution_nodes:
            institution = Institution.from_xml(institution_node)
            self.institutions.append(institution)
        payee_nodes = node.find('PAYEES')
        for payee_node in payee_nodes:
            payee = Payee.from_xml(payee_node)
            self.payees.append(payee)
        costcenter_nodes = node.find('COSTCENTERS')
        for costcenter_node in costcenter_nodes:
            costcenter = CostCenter.from_xml(costcenter_node)
            self.costCenters.append(costcenter)
        tag_nodes = node.find('TAGS')
        for tag_node in tag_nodes:
            tag = Tag.from_xml(tag_node)
            self.tags.append(tag)
        account_nodes = node.find('ACCOUNTS')
        for account_node in account_nodes:
            account = Account.from_xml(account_node)
            self.accounts.append(account)
        transaction_nodes = node.find('TRANSACTIONS')
        for transaction_node in transaction_nodes:
            transaction = Transaction.from_xml(transaction_node)
            self.transactions.append(transaction)
        self.keyValuePairs = pairs_dict_from_xml(node.find('KEYVALUEPAIRS'))

    @classmethod
    def from_kmy_file(cls, file_name):
        file_open = gzip.open if is_gz_file(file_name) else open
        with file_open(file_name, 'rb') as file:
            tree = elementTree.parse(file)
        root = tree.getroot()
        kmm = Kmy.from_xml(root)
        return kmm

def is_gz_file(filepath):
    with open(filepath, 'rb') as test_f:
        return test_f.read(2) == b'\x1f\x8b'
