from typing import Dict
from typing import List

from .payeeaddress import PayeeAddress


class Payee:
    def __init__(self):
        self.reference: str = ""
        self.name: str = ""
        self.email: str = ""
        self.id: str = ""
        self.matchingEnabled: bool = False
        self.address: PayeeAddress = PayeeAddress()
        self.payeeIdentifiers: List[Dict[str, str]] = list()
        self.usingMatchkey: bool = False
        self.matchkeys: List[str]

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

    @classmethod
    def from_xml(cls, node):
        payee = cls()
        payee.init_from_xml(node)
        return payee

    def init_from_xml(self, node):
        self.reference = node.attrib['reference']
        self.name = node.attrib['name']
        self.email = node.attrib['email']
        self.id = node.attrib['id']
        self.matchingEnabled = (node.attrib['matchingenabled'] != '0')
        self.usingMatchkey = (node.attrib["usingmatchkey"] != "0") if "usingmatchkey" in node.attrib else False
        self.matchkeys = node.attrib["matchkey"].split("&#xa;") if "matchkeys" in node.attrib else []
        address_node = node.find('ADDRESS')
        if address_node is not None:
            self.address = PayeeAddress.from_xml(address_node)
        payee_identifier_nodes = node.findall("payeeIdentifier")
        if payee_identifier_nodes is not None:
            for payee_identifier_node in payee_identifier_nodes:
                self.payeeIdentifiers.append(payee_identifier_node.attrib.copy())

    def matched_by(self, **kwargs: Dict[str, str]) -> bool:
        def is_match(candidate: Dict[str, str]) -> bool:
            for key, val in kwargs.items():
                if candidate.get(key, None) != val:
                    return False
            return True

        for identifier in self.payeeIdentifiers:
            if is_match(identifier):
                return True

        return False
