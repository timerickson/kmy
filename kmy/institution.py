from typing import Dict
from typing import List

from .institutionaddress import InstitutionAddress
from .pairs import pairs_dict_from_xml


class Institution:
    def __init__(self):
        self.id: str = ""
        self.sortCode: str = ""
        self.name: str = ""
        self.manager: str = ""
        self.address: InstitutionAddress = InstitutionAddress()
        self.accountIds: List[str] = []
        self.keyValuePairs: Dict[str, str] = {}

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

    @classmethod
    def from_xml(cls, node):
        institution = cls()
        institution.init_from_xml(node)
        return institution

    def init_from_xml(self, node):
        self.id = node.attrib['id']
        self.sortCode = node.attrib['sortcode']
        self.name = node.attrib['name']
        self.manager = node.attrib['manager']
        address_node = node.find('ADDRESS')
        if address_node is not None:
            self.address = InstitutionAddress.from_xml(address_node)
        account_id_nodes = node.find('ACCOUNTIDS')
        for account_id_node in account_id_nodes:
            self.accountIds.append(account_id_node.attrib['id'])
        self.keyValuePairs = pairs_dict_from_xml(node.find('KEYVALUEPAIRS'))
