import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.league_database import LeagueDatabase
from CurlingLeague.team import Team
from CurlingLeague.team_member import TeamMember

from PyQt5 import uic, QtWidgets

UI_MainWindow, QtBaseWindow = uic.loadUiType("member_editor.ui")


class MemberEditor(QtBaseWindow, UI_MainWindow):
    def __init__(self, member=None, team=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = LeagueDatabase.instance()
        if member:
            self.member = member
            self.team = team
            self.member_name_lineedit.setText(self.member.name)
            self.member_email_lineedit.setText(self.member.email)
            self.buttons.accepted.connect(self.update_member)

    def update_member(self):
        if self.member_name_lineedit.text() and self.member_email_lineedit.text():
            self.member.name = self.member_name_lineedit.text()
            self.member.email = self.member_email_lineedit.text()

    def new_member(self):
        if self.member_name_lineedit.text() and self.member_email_lineedit.text():
            memb = TeamMember(self.db.next_oid(), self.member_name_lineedit.text(),
                              self.member_email_lineedit.text())
            self.team.add_member(memb)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MemberEditor(TeamMember(1300, "smashers", "smashers@smashers.com"), Team(1200, "Hulks"))
    window.show()
    sys.exit(app.exec_())

