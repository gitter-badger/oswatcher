from py2neo.ogm import GraphObject, Property, RelatedTo

class Inode(GraphObject):

    def __init__(self, guestfs, filepath):
        super().__init__()
        s_filepath = str(filepath)
        name = filepath.name
        # root ?
        if not name:
            name = filepath.anchor
        self.name = name
        if guestfs.is_file(s_filepath):
            # checksums
            self.md5sum = guestfs.checksum('md5', s_filepath)
            self.sha1sum = guestfs.checksum('sha1', s_filepath)
            self.sha256sum = guestfs.checksum('sha256', s_filepath)
            self.sha512sum = guestfs.checksum('sha512', s_filepath)

        # l -> if symbolic link, returns info about the link itself
        stat = guestfs.lstatns(s_filepath)
        self.size = stat['st_size']



    # properties
    name = Property()
    size = Property()
    md5sum = Property()
    sha1sum = Property()
    sha256sum = Property()
    sha512sum = Property()


    # relationships
    children = RelatedTo("Inode", "has_child")