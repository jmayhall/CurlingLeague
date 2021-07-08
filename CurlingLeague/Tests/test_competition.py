import datetime
from datetime import timedelta
import unittest
from ..competition import Competition
from ..team import Team
from ..identifiedobject import IdentifiedObject


class CompetitionTests(unittest.TestCase):
    def test_create(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)

        self.assertEqual("Here", c1.location)
        self.assertEqual(1, c1.oid)
        self.assertIsNone(c1.date_time)
        self.assertEqual(2, len(c1.teams_competing))
        self.assertIn(t1, c1.teams_competing)
        self.assertIn(t2, c1.teams_competing)
        self.assertNotIn(t3, c1.teams_competing)

        self.assertEqual("There", c2.location)
        self.assertEqual(2, c2.oid)
        self.assertEqual(now, c2.date_time)
        self.assertEqual(2, len(c2.teams_competing))
        self.assertNotIn(t1, c2.teams_competing)
        self.assertIn(t2, c2.teams_competing)
        self.assertIn(t3, c2.teams_competing)

    def test_change_venue(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)
        self.assertEqual("Here", c1.location)
        self.assertEqual("There", c2.location)
        c1.location = "Arena"
        self.assertEqual("Arena", c1.location)
        c2.location = "Stadium"
        self.assertEqual("Stadium", c2.location)

    def test_change_time(self):
        now = datetime.datetime.now()
        tmrw = datetime.datetime.now() + timedelta(days=1)
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)
        self.assertEqual(None, c1.date_time)
        self.assertEqual(now, c2.date_time)
        c1.date_time = tmrw
        self.assertEqual(tmrw, c1.date_time)
        c2.date_time = None
        self.assertEqual(None, c2.date_time)

    def test_string(self):
        now = datetime.datetime.now()
        formatted = datetime.datetime.now().strftime("%m/%d/%y")
        tmrw = datetime.datetime.now() + timedelta(days=1)
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)
        self.assertEqual("Competition at Here between Team 1 and Team 2", c1.__str__())
        self.assertEqual(f"Competition at There on {formatted} between Team 2 and Team 3", c2.__str__())