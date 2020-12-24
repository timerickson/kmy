from .address import Address


class PayeeAddress(Address):
    def __init__(self):
        super().__init__()
        self.postCode: str = ""
        self.state: str = ""

    @classmethod
    def from_xml(cls, node):
        address = cls()
        address.init_from_xml(node)
        return address

    def init_from_xml(self, node):
        super().init_from_xml(node)
        self.postCode = node.attrib['postcode']
        self.state = node.attrib['state']
