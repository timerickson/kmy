class Address:
    def __init__(self):
        self.city: str = ""
        self.street: str = ""
        self.telephone: str = ""

    @classmethod
    def from_xml(cls, node):
        address = cls()
        address.init_from_xml(node)
        return address

    def init_from_xml(self, node):
        self.city = node.attrib['city']
        self.street = node.attrib['street']
        self.telephone = node.attrib['telephone']
