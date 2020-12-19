class FileInfo:
    def __init__(self):
        self.creationDate: str or None = None
        self.lastModifiedDate: str or None = None
        self.version: str or None = None
        self.fixVersion: str or None = None

    @classmethod
    def from_xml(cls, node):
        file_info = cls()
        file_info.creationDate = node.find('CREATION_DATE').attrib['date']
        file_info.lastModifiedDate = node.find('LAST_MODIFIED_DATE').attrib['date']
        file_info.version = node.find('VERSION').attrib['id']
        file_info.fixVersion = node.find('FIXVERSION').attrib['id']
        return file_info
