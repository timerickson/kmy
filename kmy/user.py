from .useraddress import UserAddress


class User(object):
    def __init__(self):
        self.email: str or None = None
        self.name: str or None = None
        self.address: UserAddress or None = None

    @classmethod
    def from_xml(cls, node):
        user = cls()
        user.email = node.attrib['email']
        user.name = node.attrib['name']
        user.address = UserAddress.from_xml(node.find('ADDRESS'))
        return user
