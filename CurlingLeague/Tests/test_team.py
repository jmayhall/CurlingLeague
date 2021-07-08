from ..team import Team
from ..team_member import TeamMember
from ..exceptions import DuplicateOid
from ..exceptions import DuplicateEmail
import io
import sys
import unittest


class TeamTests(unittest.TestCase):
    def test_create(self):
        name = "Curl Jam"
        oid = 10
        t = Team(oid, name)
        self.assertEqual(name, t.name)
        self.assertEqual(oid, t.oid)

    def test_change_name(self):
        name = "Curl Jam"
        oid = 10
        t = Team(oid, name)
        self.assertEqual(name, t.name)
        t.name = "Sliders"
        self.assertEqual("Sliders", t.name)

    def test_if_same_team_based_on_oid(self):
        name = "Curl Jam"
        oid = 10
        t = Team(oid, name)
        name = "Sliders"
        oid = 10
        t2 = Team(oid, name)
        name = "Terminators"
        oid = 11
        t3 = Team(oid, name)
        self.assertTrue(t == t2)
        self.assertTrue(t != t3)

    def test_adding_adds_to_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        self.assertIn(tm1, t.members)
        self.assertNotIn(tm2, t.members)
        t.add_member(tm2)
        self.assertIn(tm1, t.members)
        self.assertIn(tm2, t.members)

    def test_adding_members_doesnt_duplicate(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        self.assertIn(tm1, t.members)
        self.assertIn(tm2, t.members)
        self.assertEqual(2, len(t.members))
        with self.assertRaises(Exception):
            t.add_member(tm2)
        with self.assertRaises(Exception):
            t.add_member(tm1)
        self.assertEqual(2, len(t.members))

    def test_removing_removes_from_members(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        self.assertEqual(2, len(t.members))
        t.remove_member(tm1)
        self.assertNotIn(tm1, t.members)
        self.assertIn(tm2, t.members)
        self.assertEqual(1, len(t.members))

    def test_string(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "g")
        t.add_member(tm1)
        t.add_member(tm2)
        self.assertEqual("Flintstones: 2 members", t.__str__())

    def test_duplicate_email(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "f")
        tm3 = TeamMember(5, "z", "z")
        t.add_member(tm1)
        self.assertIn(tm1, t.members)
        with self.assertRaises(DuplicateEmail):
            t.add_member(tm2)


    def test_duplicate_oid(self):
        t = Team(1, "Flintstones")
        tm1 = TeamMember(5, "f", "f")
        tm2 = TeamMember(6, "g", "f")
        tm3 = TeamMember(5, "z", "z")
        t.add_member(tm1)
        self.assertIn(tm1, t.members)
        with self.assertRaises(DuplicateOid):
            t.add_member(tm3)

