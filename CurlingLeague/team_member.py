from CurlingLeague.identifiedobject import IdentifiedObject


class TeamMember(IdentifiedObject):
    """Team Member object class
    Defines the Team Member Object"""

    def __init__(self, oid, name, email):
        if oid is not None and name is not None:
            super().__init__(oid)
            self._name = name
            self._email = email

    def __str__(self):
        name = self._name
        email = "no email address"
        if self._email:
            email = self._email
        return name + "<" + email + ">"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None:
            self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def send_email(self, emailer, subject, message):
        rec = [self._email]
        emailer.send_plain_email(rec, subject, message)
