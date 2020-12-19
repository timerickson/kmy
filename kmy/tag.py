from .payeeaddress import PayeeAddress


class Tag:
    def __init__(self):
        self.closed: bool = False
        self.tagColor: str or None = None
        self.name: str or None = None
        self.id: str or None = None

    @classmethod
    def from_xml(cls, node):
        tag = cls()
        tag.init_from_xml(node)
        return tag

    def init_from_xml(self, node):
        self.closed = (node.attrib['closed'] != '0')
        self.tagColor = node.attrib['tagcolor']
        self.name = node.attrib['name']
        self.id = node.attrib['id']
