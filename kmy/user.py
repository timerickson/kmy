from .useraddress import UserAddress


class User(object):
    def __init__(self):
        self.email: str = ""
        self.name: str = ""
        self.address: UserAddress = UserAddress()

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}')"

    @classmethod
    def from_xml(cls, node):
        user = cls()
        user.email = node.attrib['email']
        user.name = node.attrib['name']
        user.address = UserAddress.from_xml(node.find('ADDRESS'))
        return user
