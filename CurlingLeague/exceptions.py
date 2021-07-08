class DuplicateOid(Exception):
    def __init__(self, oid):
        super().__init__(oid)
        self.oid = oid


class DuplicateEmail(Exception):
    def __init__(self, email):
        super().__init__(email)
        self.email = email

