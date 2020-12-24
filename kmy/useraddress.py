from .address import Address


class UserAddress(Address):
    def __init__(self):
        super().__init__()
        self.zipcode: str = ""
        self.county: str = ""

    @classmethod
    def from_xml(cls, node):
        address = cls()
        address.init_from_xml(node)
        return address

    def init_from_xml(self, node):
        super().init_from_xml(node)
        self.zipcode = node.attrib['zipcode']
        self.county = node.attrib['county']
