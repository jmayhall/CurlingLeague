from CurlingLeague.exceptions import DuplicateOid
from CurlingLeague.identifiedobject import IdentifiedObject


class League(IdentifiedObject):
    def __init__(self, oid, name):
        super().__init__(oid)
        self._name = name
        self._teams = []
        self._competitions = []

    def __str__(self):
        return self._name + ": " + str(len(self._teams)) + " teams, " \
               + str(len(self._competitions)) + " competitions"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name is not None:
            self._name = name

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self._competitions

    def add_team(self, team):
        try:
            if team.oid not in [x.oid for x in self._teams]:
                self._teams.append(team)
            else:
                raise DuplicateOid(team.oid)
        except DuplicateOid as ex:
            raise DuplicateOid(ex.oid)

    def delete_team(self, ndx):
        self._teams.__delitem__(ndx)

    def add_competition(self, competition):
        try:
            if competition.oid not in [x.oid for x in self._competitions]:
                self._competitions.append(competition)
            else:
                raise DuplicateOid(competition.oid)
        except DuplicateOid as ex:
            #print(f"Duplicate Competition ID: {competition.oid}")
            raise DuplicateOid(ex.oid)

    def teams_for_member(self, member):
        return [team for team in self.teams if member in team.members]

    def competitions_for_team(self, team):
        return [comp for comp in self.competitions if team in comp.teams_competing]

    def competitions_for_member(self, member):
        comps = [self.competitions_for_team(team) for team in self.teams_for_member(member)]
        return [x for y in comps for x in y]
