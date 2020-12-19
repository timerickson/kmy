from typing import List

from .split import Split


class Transaction:
    def __init__(self):
        self.postDate: str or None = None
        self.memo: str or None = None
        self.commodity: str or None = None
        self.entryDate: str or None = None
        self.id: str or None = None
        self.splits: List[Split] = []

    @classmethod
    def from_xml(cls, node):
        transaction = cls()
        transaction.init_from_xml(node)
        return transaction

    def init_from_xml(self, node):
        self.postDate = node.attrib['postdate']
        self.memo = node.attrib['memo']
        self.commodity = node.attrib['commodity']
        self.entryDate = node.attrib['entrydate']
        self.id = node.attrib['id']
        split_nodes = node.find('SPLITS')
        if split_nodes is not None:
            for split_node in split_nodes:
                split = Split.from_xml(split_node)
                self.splits.append(split)
