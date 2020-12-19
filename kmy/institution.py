from typing import List

from kmy.institutionaddress import InstitutionAddress


class Institution:
    def __init__(self):
        self.id: str or None = None
        self.sortcode: str or None = None
        self.name: str or None = None
        self.manager: str or None = None
        self.address: InstitutionAddress or None = None
        self.accountIds: List[str] = []
        self.keyValuePairs = []

    @classmethod
    def from_xml(cls, node):
        institution = cls()
        institution.init_from_xml(node)
        return institution

    def init_from_xml(self, node):
        self.id = node.attrib['id']
        self.sortcode = node.attrib['sortcode']
        self.name = node.attrib['name']
        self.manager = node.attrib['manager']
        address_node = node.find('ADDRESS')
        if address_node is not None:
            self.address = InstitutionAddress.from_xml(address_node)
        account_id_nodes = node.find('ACCOUNTIDS')
        for account_id_node in account_id_nodes:
            self.accountIds.append(account_id_node.attrib['id'])
