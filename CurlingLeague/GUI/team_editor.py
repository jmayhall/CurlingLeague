import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.GUI.member_editor import MemberEditor
from CurlingLeague.league_database import LeagueDatabase
from CurlingLeague.team import Team

from PyQt5 import uic, QtWidgets

from CurlingLeague.team_member import TeamMember

UI_MainWindow, QtBaseWindow = uic.loadUiType("team_editor.ui")


class TeamEditor(QtBaseWindow, UI_MainWindow):
    def __init__(self, team=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if team:
            self.db = LeagueDatabase.instance()
            self.team = team
            self.members = self.team.members
            self.update_ui()
            self.add_member_button.clicked.connect(self.add_member_clicked)
            self.edit_member_button.clicked.connect(self.edit_member_clicked)
            self.delete_member_button.clicked.connect(self.delete_member_clicked)

    def update_ui(self):
        self.member_listwidget.clear()
        for m in self.members:
            self.member_listwidget.addItem(str(m))

    def add_member_clicked(self):
        if self.member_name_lineedit.text() and self.member_email_lineedit.text():
            self.team.add_member(TeamMember(self.db.next_oid(), self.member_name_lineedit.text(),
                                            self.member_email_lineedit.text()))
            self.update_ui()
            self.member_name_lineedit.clear()
            self.member_email_lineedit.clear()

    def edit_member_clicked(self):
        # if self.member_name_lineedit.text() and self.member_email_lineedit.text():
        row = self.member_listwidget.currentRow()
        memb = self.members[row]
        dialog = MemberEditor(memb, self.team)
        result = dialog.exec()
        # memb.name = self.member_name_lineedit.text()
        # memb.email = self.member_email_lineedit.text()
        self.update_ui()
        # self.member_name_lineedit.clear()
        # self.member_email_lineedit.clear()

    def delete_member_clicked(self):
        row = self.member_listwidget.currentRow()
        memb = self.members[row].name
        dialog = QMessageBox(QMessageBox.Icon.Information,
                             "Confirm Delete",
                             f"The member \"{memb}\" will be deleted!",
                             QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.team.delete_member(row)
            self.update_ui()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TeamEditor(Team(1200, "smashers"))
    window.show()
    sys.exit(app.exec_())
