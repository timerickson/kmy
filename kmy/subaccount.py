class SubAccount:
    def __init__(self):
        self.id: str = ""

    @classmethod
    def from_xml(cls, node):
        subaccount = cls()
        subaccount.init_from_xml(node)
        return subaccount

    def init_from_xml(self, node):
        self.id = node.attrib['id']
