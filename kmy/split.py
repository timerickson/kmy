from .payeeaddress import PayeeAddress
from .subaccount import SubAccount


class Split:
    def __init__(self):
        self.payee: str or None = None
        self.memo: str or None = None
        self.shares: str or None = None
        self.number: str or None = None
        self.action: str or None = None
        self.price: str or None = None
        self.account: str or None = None
        self.reconcileFlag: str or None = None
        self.bankId: str or None = None
        self.value: str or None = None
        self.reconcileDate: str or None = None
        self.id: str or None = None

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
