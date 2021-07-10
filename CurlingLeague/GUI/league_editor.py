import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.GUI.team_editor import TeamEditor
from CurlingLeague.league import League

from PyQt5 import uic, QtWidgets

from CurlingLeague.league_database import LeagueDatabase
from CurlingLeague.team import Team

UI_MainWindow, QtBaseWindow = uic.loadUiType("league_editor.ui")


class LeagueEditor(QtBaseWindow, UI_MainWindow):
    def __init__(self, league=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if league:
            self.db = LeagueDatabase.instance()
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
        team = Team(self.db.next_oid(), self.add_team_lineedit.text())
        self.league.add_team(team)
        self.update_ui()
        self.add_team_lineedit.clear()
        dialog = TeamEditor(team)
        result = dialog.exec()
        self.update_ui()

    def edit_team_clicked(self):
        row = self.teams_listwidget.currentRow()
        team = self.teams[row]
        dialog = TeamEditor(team)
        result = dialog.exec()
        self.update_ui()

    def delete_team_clicked(self):
        row = self.teams_listwidget.currentRow()
        team = self.teams[row].name
        dialog = QMessageBox(QMessageBox.Icon.Information,
                             "Confirm Delete",
                             f"The team \"{team}\" will be deleted!",
                             QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.league.delete_team(row)
            self.update_ui()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LeagueEditor(League(1200,"smashers"))
    window.show()
    sys.exit(app.exec_())
