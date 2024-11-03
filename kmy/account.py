from typing import Dict
from typing import List

from .pairs import pairs_dict_from_xml
from .subaccount import SubAccount


class Account:
    def __init__(self):
        self.number: str = ""
        self.lastModified: str = ""
        self.institution: str = ""
        self.name: str = ""
        self.currency: str = ""
        self.parentAccount: str = ""
        self.lastReconciled: str = ""
        self.description: str = ""
        self.type: str = ""
        self.opened: str = ""
        self.id: str = ""
        self.subAccounts: List[SubAccount] = []
        self.keyValuePairs: Dict[str, str] = {}

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', currency={self.currency})"

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
        self.keyValuePairs = pairs_dict_from_xml(node.find('KEYVALUEPAIRS'))
