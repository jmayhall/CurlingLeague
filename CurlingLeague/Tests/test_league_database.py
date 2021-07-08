import unittest
from ..league_database import LeagueDatabase
from ..league import League
from ..team import Team
from ..team_member import TeamMember
from ..competition import Competition


class LeagueDatabaseTests(unittest.TestCase):
    db = LeagueDatabase.instance()
    db2 = LeagueDatabase.instance()

    def test_create(self):
        self.assertTrue(self.db)

    def test_is_singleton(self):
        self.assertIs(self.db, self.db2)

    def test_add_league(self):
        league = League(self.db.next_oid(), "All Valley")
        self.db.add_league(league)
        t1 = Team(self.db.next_oid(), "Sluggers")
        league.add_team(t1)
        t2 = Team(self.db.next_oid(), "Smashers")
        league.add_team(t2)
        t3 = Team(self.db.next_oid(), "Tigers")
        league.add_team(t3)
        t4 = Team(self.db.next_oid(), "Tiggers")
        league.add_team(t4)

        m1 = TeamMember(self.db.next_oid(), "Jeff", "jmayhall@gmail.com")
        m2 = TeamMember(self.db.next_oid(), "Corri", "corrimayhall@gmail.com")

        t1.add_member(m1)
        t1.add_member(m2)

        l1 = [t1, t2]
        l2 = [t1, t3]
        l3 = [t2, t3]
        #
        c1 = Competition(self.db.next_oid(), l1, "Arena1", None)
        c2 = Competition(self.db.next_oid(), l2, "Arena2", None)
        c3 = Competition(self.db.next_oid(), l3, "Stadium", None)
        c4 = Competition(self.db.next_oid(), l3, "StadiumGreen", None)
        #
        league.add_competition(c1)
        league.add_competition(c2)
        league.add_competition(c3)
        league.add_competition(c4)

        self.assertEqual([league], self.db.leagues)

        league2 = League(self.db.next_oid(), "Beach League")
        self.db.add_league(league2)

        self.assertEqual([league, league2], self.db.leagues)


