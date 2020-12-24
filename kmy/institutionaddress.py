from .address import Address


class InstitutionAddress(Address):
    def __init__(self):
        super().__init__()
        self.zip: str = ""

    @classmethod
    def from_xml(cls, node):
        address = cls()
        address.init_from_xml(node)
        return address

    def init_from_xml(self, node):
        super().init_from_xml(node)
        self.zip = node.attrib['zip']
