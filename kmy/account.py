from typing import List

from .payeeaddress import PayeeAddress
from .subaccount import SubAccount


class Account:
    def __init__(self):
        self.number: str or None = None
        self.lastModified: str or None = None
        self.institution: str or None = None
        self.name: str or None = None
        self.currency: str or None = None
        self.parentAccount: str or None = None
        self.lastReconciled: str or None = None
        self.description: str or None = None
        self.type: str or None = None
        self.opened: str or None = None
        self.id: str or None = None
        self.subAccounts: List[SubAccount] = []

    @classmethod
    def from_xml(cls, node):
        account = cls()
        account.init_from_xml(node)
        return account

    def init_from_xml(self, node):
        self.number = node.attrib['number']
        self.lastModified = node.attrib['lastmodified']
        self.institution = node.attrib['institution']
        self.name = node.attrib['name']
        self.currency = node.attrib['currency']
        self.parentAccount = node.attrib['parentaccount']
        self.lastReconciled = node.attrib['lastreconciled']
        self.description = node.attrib['description']
        self.type = node.attrib['type']
        self.opened = node.attrib['opened']
        self.id = node.attrib['id']
        subaccount_nodes = node.find('SUBACCOUNTS')
        if subaccount_nodes is not None:
            for subaccount_node in subaccount_nodes:
                subaccount = SubAccount.from_xml(subaccount_node)
                self.subAccounts.append(subaccount)
