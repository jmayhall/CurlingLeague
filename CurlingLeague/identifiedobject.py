class IdentifiedObject:
    """Abstract Class for comparing object IDs"""

    def __init__(self, oid):
        self._oid = oid

    def __eq__(self, other):
        return type(self) == type(other) and self.oid == other.oid

    def __hash__(self):
        return hash(self._oid)

    @property
    def oid(self):
        return self._oid
