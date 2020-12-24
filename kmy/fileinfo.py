class FileInfo:
    def __init__(self):
        self.creationDate: str = ""
        self.lastModifiedDate: str = ""
        self.version: str = ""
        self.fixVersion: str = ""

    @classmethod
    def from_xml(cls, node):
        file_info = cls()
        file_info.creationDate = node.find('CREATION_DATE').attrib['date']
        file_info.lastModifiedDate = node.find('LAST_MODIFIED_DATE').attrib['date']
        file_info.version = node.find('VERSION').attrib['id']
        file_info.fixVersion = node.find('FIXVERSION').attrib['id']
        return file_info
