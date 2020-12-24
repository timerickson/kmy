class Split:
    def __init__(self):
        self.payee: str = ""
        self.memo: str = ""
        self.shares: str = ""
        self.number: str = ""
        self.action: str = ""
        self.price: str = ""
        self.account: str = ""
        self.reconcileFlag: str = ""
        self.bankId: str = ""
        self.value: str = ""
        self.reconcileDate: str = ""
        self.id: str = ""

    @classmethod
    def from_xml(cls, node):
        split = cls()
        split.init_from_xml(node)
        return split

    def init_from_xml(self, node):
        self.payee = node.attrib['payee']
        self.memo = node.attrib['memo']
        self.shares = node.attrib['shares']
        self.number = node.attrib['number']
        self.action = node.attrib['action']
        self.price = node.attrib['price']
        self.account = node.attrib['account']
        self.reconcileFlag = node.attrib['reconcileflag']
        self.bankId = node.attrib['bankid']
        self.value = node.attrib['value']
        self.reconcileDate = node.attrib['reconciledate']
        self.id = node.attrib['id']
