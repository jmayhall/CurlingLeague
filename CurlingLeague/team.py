from CurlingLeague.identifiedobject import IdentifiedObject
from CurlingLeague.exceptions import DuplicateEmail
from CurlingLeague.exceptions import DuplicateOid


class Team(IdentifiedObject):
    """Team Object Class
    Defines the Team Object with properties:
    Name: Name of the team
    Members: List of members on the team"""

    def __init__(self, oid, name):
        if oid is not None and name is not None:
            super().__init__(oid)
            self._name = name
            self._members = []

    def __str__(self):
        return self._name + ": " + str(len(self._members)) + " members"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = name

    @property
    def members(self):
        return self._members

    def add_member(self, member):
        email_valid = False
        oid_valid = False
        try:
            if member.email not in [x.email for x in self._members]:
                email_valid = True
            else:
                raise DuplicateEmail(member.email)
        except DuplicateEmail as ex:
            raise DuplicateEmail(ex.email)
        try:
            if member.oid not in [x.oid for x in self._members]:
                oid_valid = True
            else:
                raise DuplicateOid(member.oid)
        except DuplicateOid as ex:
            raise DuplicateOid(ex.oid)

        if email_valid and oid_valid:
            self.members.append(member)

    def delete_member(self, ndx):
        self._members.__delitem__(ndx)

    def remove_member(self, member):
        if member in self.members:
            self.members.remove(member)

    def send_email(self, emailer, subject, message):
        rec = [member.email for member in self.members if member.email is not None]
        emailer.send_plain_email(rec, subject, message)
