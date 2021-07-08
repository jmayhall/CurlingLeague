import unittest
from ..team_member import TeamMember


class TeamMemberTests(unittest.TestCase):
    def test_create(self):
        oid = 1
        name = "Fred"
        email = "fred.flintstone@gmail.com"
        tm = TeamMember(oid, name, email)
        self.assertEqual(oid, tm.oid)
        self.assertEqual(name, tm.name)
        self.assertEqual(email, tm.email)

    def test_name_change(self):
        tm = TeamMember(1, "Jason", "jason@auburn.edu")
        self.assertEqual(tm.name, "Jason")
        self.assertNotEqual(tm.name, "Bob")
        tm.name = "Matt"
        self.assertEqual(tm.name, "Matt")
        self.assertNotEqual(tm.name, "Jason")

    def test_email_change(self):
        tm = TeamMember(1, "Jason", "jason@auburn.edu")
        self.assertEqual("jason@auburn.edu", tm.email)
        self.assertNotEqual("bob@auburn.edu", tm.email)
        tm.email = "matt@auburn.edu"
        self.assertEqual("matt@auburn.edu", tm.email)
        self.assertNotEqual("jason@auburn.edu", tm.email)

    def test_equality_based_on_id(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(2, "name", "email")

        # team members must be equal to themselves
        self.assertTrue(tm_1 == tm_1)
        self.assertTrue(tm_2 == tm_2)
        self.assertTrue(tm_3 == tm_3)

        # same id are equal, even if other fields different
        self.assertTrue(tm_1 == tm_2)

        # different ids are not equal, even if other fields the same
        self.assertTrue(tm_1 != tm_3)

    def test_hash_based_on_id(self):
        tm_1 = TeamMember(1, "name", "email")
        tm_2 = TeamMember(1, "other name", "other email")
        tm_3 = TeamMember(2, "name", "email")

        # hash depends only on id
        self.assertTrue(hash(tm_1) == hash(tm_2))

        # objects with different id's may have different hash codes
        # note: this is not a requirement of the hash function but
        # for the case of id == 1 and id == 2 we can verify that their
        # hash codes are different in a REPL (just print(hash(1)) etc).
        self.assertTrue(hash(tm_1) != hash(tm_3))

    def test_string(self):
        tm = TeamMember(1, "Jason", "jason@auburn.edu")
        self.assertEqual("Jason<jason@auburn.edu>", tm.__str__())


if __name__ == '__main__':
    unittest.main()
