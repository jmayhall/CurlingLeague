from CurlingLeague.identifiedobject import IdentifiedObject


class Competition(IdentifiedObject):
    """Competition Object Class
    Defines the Competition Object"""

    def __init__(self, oid, teams, location, datetime):
        super().__init__(oid)
        self._teams_competing = teams
        self._location = location
        self._datetime = datetime

    def __str__(self):
        dt = ""
        if self._datetime:
            dt = " on " + self._datetime.strftime("%m/%d/%y")
        return "Competition at " + self._location + dt \
            + " between " + self._teams_competing[0].name + " and " \
            + self._teams_competing[1].name

    @property
    def teams_competing(self):
        return self._teams_competing

    @property
    def date_time(self):
        return self._datetime

    @date_time.setter
    def date_time(self, datetime):
        self._datetime = datetime

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location):
        self._location = location

    def send_email(self, emailer, subject, message):
        rec = [member.email for teams in self._teams_competing for member in teams.members]
        emailer.send_plain_email(rec, subject, message)
