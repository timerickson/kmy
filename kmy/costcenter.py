class CostCenter:
    def __init__(self):
        pass

    @classmethod
    def from_xml(cls, node):
        costcenter = cls()
        costcenter.init_from_xml(node)
        return costcenter

    def init_from_xml(self, node):
        pass
