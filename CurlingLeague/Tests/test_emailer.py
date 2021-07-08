import unittest
from ..league_database import LeagueDatabase
from ..league import League
from ..team import Team
from ..team_member import TeamMember
from ..competition import Competition
from ..emailer import Emailer


class LeagueDatabaseTests(unittest.TestCase):
    db = LeagueDatabase.instance()
    db2 = LeagueDatabase.instance()

    def test_send_email(self):
        # A keyring record is required for gmail account
        # Be sure to add a keyring entry
        # The keyring service name can be passed as an optional 4th argument to send_plain_email
        mailer = Emailer.instance()
        mailer.configure("jzm0162@gmail.com")
        mailer.send_plain_email(["jmayhall@gmail.com"], "Next Match", "Next match is Sunday!!", "gmail")
