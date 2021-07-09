import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.GUI.team_editor import TeamEditor
from CurlingLeague.league import League

from PyQt5 import uic, QtWidgets

from CurlingLeague.team import Team

UI_MainWindow, QtBaseWindow = uic.loadUiType("league_editor.ui")


class LeagueEditor(QtBaseWindow, UI_MainWindow):
    def __init__(self, league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if league:
            self.league = league
            self.teams = self.league.teams
            self.update_ui()
            self.add_team_button.clicked.connect(self.add_team_clicked)
            self.edit_team_button.clicked.connect(self.edit_team_clicked)
            self.delete_team_button.clicked.connect(self.delete_team_clicked)

    def update_ui(self):
        self.teams_listwidget.clear()
        for t in self.teams:
            self.teams_listwidget.addItem(str(t))

    def add_team_clicked(self):
        self.league.add_team(self.db.next_oid(), self.add_team_lineedit.text())
        self.update_ui()
        self.add_team_lineedit.clear()

    def edit_team_clicked(self):
        row = self.teams_listwidget.currentRow()
        team = self.teams[row]
        dialog = TeamEditor(team)
        result = dialog.exec()

    def delete_team_clicked(self):
        pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LeagueEditor(League(1200,"smashers"))
    window.show()
    sys.exit(app.exec_())
