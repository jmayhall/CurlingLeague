import datetime
from pprint import pprint

from league import League
from competition import Competition
from CurlingLeague.exceptions import DuplicateOid
from team import Team
from team_member import TeamMember
from emailer import Emailer
from league_database import LeagueDatabase

if __name__ == "__main__":
    LeagueDatabase.load("leaguedb")
    db = LeagueDatabase.instance()

    print(len(db.leagues))

    db.import_league("Snarl Champions", "Teams.csv")
    db.import_league("Snarl Champions", "Teams.csv")
    db.import_league("Snarl Champions", "Teams.csv")
    db.import_league("Snarl Champions", "Teams.csv")
    db.import_league("Snarl Champions", "Teams.csv")
    # for i in range(1000):
    #     i = i + 1000
    #     name = "league" + str(i)
    #     try:
    #         db.add_league(League(db.next_oid(), name))
    #     except DuplicateOid:
    #         pass
    print(f"imported 5 leagues")
    print(len(db.leagues))
    # print(db.leagues)
    #
    # db.save("leaguedb")
    # print("...saved db")
    # print("imported league")
    # print(db.leagues)

    # # league = League(db.next_oid(), "Snarl Champions")

    # db2 = LeagueDatabase.instance()
    # db._leagues = []
    # db2.load("leaguedb.dat")
    # db2.load("leaguedb.dat")
    # print(f"DB2: {db2.leagues}")
    #
    # db2.load("leaguedb.dat")
    # print(db2.leagues)
    league = db.leagues[0]
    league2 = db.leagues[1]
    league3 = db.leagues[2]
    league4 = db.leagues[3]

    t1 = Team(0, "Sluggers")
    # league.add_team(t1)
    t2 = Team(1, "Smashers")
    # league.add_team(t2)
    t3 = Team(2, "Tigers")
    # league.add_team(t3)
    t4 = Team(2, "Tiggers")
    # league.add_team(t4)

    m1 = TeamMember(10, "Jeff", "jmayhall@gmail.com")
    m2 = TeamMember(11, "Corri", "corrimayhall@gmail.com")
    # m3 = TeamMember(12, "Brad", "btmayhall@gmail.com")
    # m4 = TeamMember(13, "Billy", "brmayhall@gmail.com")
    # m5 = TeamMember(14, "Sam", "sam@super.net")
    # m6 = TeamMember(15, "Dean", "dean")
    # m7 = TeamMember(10, "Sparrow", "jack@pirates.com")

    # t1.add_member(m1)
    # t1.add_member(m7)
    # t1.add_member(m2)
    # t2.add_member(m3)
    # t2.add_member(m4)
    # t3.add_member(m5)
    # t3.add_member(m6)
    # t3.add_member(m1)
    # t1.add_member(m1)

    l1 = [t1, t2]
    l2 = [t1, t3]
    l3 = [t2, t3]
    #
    c1 = Competition(db.next_oid(), l1, "Arena1", datetime.datetime.now())
    c2 = Competition(db.next_oid(), l2, "Arena2", datetime.datetime.now())
    c3 = Competition(db.next_oid(), l3, "Stadium", None)
    c4 = Competition(db.next_oid(), l3, "StadiumGreen", None)
    #
    league.add_competition(c1)
    league.add_competition(c2)
    league.add_competition(c3)
    league.add_competition(c4)

    # m9 = TeamMember(18, "Jack", "jack")
    # t2.add_member(m1)

    db.export_league(db.leagues[0], "Teamsv2.csv")
    print("exported league")
    # mailer = Emailer.instance()
    # mailer.configure("jzm0162@gmail.com")
    # mailer.send_plain_email(["jmayhall@gmail.com"], "Next Match", "Bring some beer")

    # db.save("leaguedb")
