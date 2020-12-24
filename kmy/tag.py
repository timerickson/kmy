class Tag:
    def __init__(self):
        self.closed: bool = False
        self.tagColor: str = ""
        self.name: str = ""
        self.id: str = ""

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
