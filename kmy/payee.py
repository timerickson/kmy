from .payeeaddress import PayeeAddress


class Payee:
    def __init__(self):
        self.reference: str = ""
        self.name: str = ""
        self.email: str = ""
        self.id: str = ""
        self.matchingEnabled: bool = False
        self.address: PayeeAddress = PayeeAddress()

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
        address_node = node.find('ADDRESS')
        if address_node is not None:
            self.address = PayeeAddress.from_xml(address_node)
