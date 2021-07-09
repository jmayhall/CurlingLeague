import pickle
import csv
import os.path

from CurlingLeague.league import League
from CurlingLeague.team import Team
from CurlingLeague.team_member import TeamMember
from CurlingLeague.exceptions import DuplicateOid


class LeagueDatabase:
    _sole_instance = None

    def __init__(self):
        self._leagues = []
        self._last_oid = 0

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    @classmethod
    def load(cls, file_name):
        try:
            with open(file_name, mode="rb") as f:
                tmp = pickle.load(f)
                cls._sole_instance = tmp
        except FileNotFoundError:
            if os.path.isfile(file_name):
                with open(file_name + ".backup", mode="rb") as f:
                    tmp = pickle.load(f)
                    cls._sole_instance = tmp
                    return cls._sole_instance
                print("File Not Found!  Loading from backup")
            else:
                print("Nothing to load")

    def save(self, file_name):
        if os.path.isfile(file_name + ".backup"):
            os.remove(file_name + ".backup")
        if os.path.isfile(file_name):
            os.rename(file_name, file_name + ".backup")
        with open(file_name, mode="wb") as f:
            pickle.dump(self, f)

    @property
    def leagues(self):
        return self._leagues

    def add_league(self, league):
        try:
            if league not in self._leagues:
                self._leagues.append(league)
            else:
                raise DuplicateOid(league.oid)
        except DuplicateOid as ex:
            # raise DuplicateOid(ex.oid)
            print(f"Duplicate League ID: {league.oid}")

    def delete_league(self, ndx):
        self._leagues.__delitem__(ndx)

    def next_oid(self):
        self._last_oid += 1
        return self._last_oid

    def import_league(self, league_name, file_name):
        leag = League(self.next_oid(), league_name)
        try:
            imported = []
            with open(file_name, newline='', encoding='utf-8') as cf:
                spamreader = csv.reader(cf, delimiter=',', quotechar='"')
                for row in spamreader:
                    imported.append((row[0], row[1], row[2]))
        except FileNotFoundError:
            print("File Not Found! - Nothing Imported!")
        except Exception:
            print("There was an error importing the league")

        # Parse imported Data
        # imported = imported.sort()
        last_team = ""
        tm = None
        for x in imported[1:]:
            if x[0] is not last_team:
                tm = Team(self.next_oid(), x[0])
                leag.add_team(tm)
                last_team = tm.name
            m = TeamMember(self.next_oid(), x[1], x[2])
            tm.add_member(m)

        # Add League to League Database
        self.add_league(leag)

    def export_league(self, league, file_name):
        to_export = []
        for t in league.teams:
            for m in t.members:
                to_export.append((t.name, m.name, m.email))
        try:
            with open(file_name, 'w', newline='', encoding='utf-8') as cf:
                spamwriter = csv.writer(cf, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(("Team name", "Member name", "Member email"))
                for row in to_export:
                    spamwriter.writerow(row)
        except Exception:
            print("There was an error exporting the league")
