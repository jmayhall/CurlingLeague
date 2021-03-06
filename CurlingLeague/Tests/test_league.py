import unittest

from ..competition import Competition
from ..league import League
from ..team import Team
from ..team_member import TeamMember
from ..exceptions import DuplicateOid


class LeagueTests(unittest.TestCase):
    def test_create(self):
        league = League(1, "AL State Curling League")
        self.assertEqual(1, league.oid)
        self.assertEqual("AL State Curling League", league.name)
        self.assertEqual([], league.teams)
        self.assertEqual([], league.competitions)

    def test_change_name(self):
        league = League(1, "AL State Curling League")
        self.assertEqual(1, league.oid)
        self.assertEqual("AL State Curling League", league.name)
        league.name = "Auburn Curling League"
        self.assertEqual("Auburn Curling League", league.name)
        self.assertNotEqual("AL State Curling League", league.name)

    def test_adding_team_adds_to_teams(self):
        t = Team(1, "Ice Maniacs")
        league = League(1, "AL State Curling League")
        self.assertNotIn(t, league.teams)
        league.add_team(t)
        self.assertIn(t, league.teams)
        t2 = Team(2, "Brooms Maniacs")
        t3 = Team(3, "Stone Maniacs")
        t4 = Team(4, "Maniacs")
        t5 = Team(5, "woManiacs")
        league.add_team(t2)
        league.add_team(t3)
        league.add_team(t4)
        league.add_team(t5)
        self.assertIn(t5, league.teams)
        self.assertEqual(5, len(league.teams))

    def test_adding_competition_adds_to_competitions(self):
        c = Competition(1, [], "Local tourney", None)
        league = League(13, "AL State Curling League")
        self.assertNotIn(c, league.competitions)
        league.add_competition(c)
        c2 = Competition(2, [], "Local tourney", None)
        c3 = Competition(3, [], "Local tourney", None)
        league.add_competition(c2)
        league.add_competition(c3)
        self.assertIn(c, league.competitions)
        self.assertEqual(3, len(league.competitions))

    @staticmethod
    def build_league():
        league = League(1, "Some league")
        t1 = Team(1, "t1")
        t2 = Team(2, "t2")
        t3 = Team(3, "t3")
        all_teams = [t1, t2, t3]
        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)
        # every team plays every other team twice
        oid = 1
        for c in [Competition(oid := oid + 1, [team1, team2], team1.name + " vs " + team2.name, None)
                  for team1 in all_teams
                  for team2 in all_teams
                  if team1 != team2]:
            league.add_competition(c)
        return league

    def test_big_league(self):
        league = self.build_league()
        t = league.teams[0]
        cs = league.competitions_for_team(t)
        # matchups are (t1, t2), (t1, t3), (t2, t1), (t3, t1) but we don't know what order they will be returned in
        # so use sets.
        cs_names = {c.location for c in cs}  # set comprehension
        self.assertEqual({"t1 vs t2", "t1 vs t3", "t2 vs t1", "t3 vs t1"}, cs_names)

        self.assertEqual([league.teams[2]], league.teams_for_member(league.teams[2].members[0]))

        # Grab a player from the third team
        cs = league.competitions_for_member(league.teams[2].members[0])
        # matchups are (t3, t1), (t3, t2), (t2, t3), (t1, t3) but we don't know what order they will be returned in
        # so use sets.
        cs_names = {c.location for c in cs}  # set comprehensionq
        self.assertEqual({"t3 vs t1", "t3 vs t2", "t2 vs t3", "t1 vs t3"}, cs_names)

    def test_string(self):
        league = League(13, "AL State Curling League")
        c = Competition(1, [], "Local tourney", None)
        c2 = Competition(2, [], "Local tourney", None)
        c3 = Competition(3, [], "Local tourney", None)
        t1 = Team(1, "t1")
        t2 = Team(2, "t2")
        t3 = Team(3, "t3")
        league.add_competition(c)
        league.add_competition(c2)
        league.add_competition(c3)
        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        self.assertIn(c, league.competitions)
        self.assertEqual(3, len(league.competitions))
        self.assertEqual("AL State Curling League: 3 teams, 3 competitions", league.__str__())

    def test_duplicate_team(self):
        league = League(13, "AL State Curling League")
        t1 = Team(1, "Flintstones")
        t2 = Team(1, "Jetsons")
        league.add_team(t1)
        with self.assertRaises(DuplicateOid):
            league.add_team(t2)

    def test_duplicate_competition(self):
        league = League(13, "AL State Curling League")
        c = Competition(1, [], "Local tourney", None)
        c2 = Competition(2, [], "Local tourney", None)
        c3 = Competition(1, [], "Local tourney", None)
        league.add_competition(c)
        league.add_competition(c2)
        with self.assertRaises(DuplicateOid):
            league.add_competition(c3)
