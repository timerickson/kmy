class SubAccount:
    def __init__(self):
        self.id: str = ""

    def __repr__(self):
        return f"{self.__class__.__name__}(id='{self.id}')"

    @classmethod
    def from_xml(cls, node):
        subaccount = cls()
        subaccount.init_from_xml(node)
        return subaccount

    def init_from_xml(self, node):
        self.id = node.attrib['id']
