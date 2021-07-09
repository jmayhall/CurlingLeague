import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.team import Team

from PyQt5 import uic, QtWidgets

UI_MainWindow, QtBaseWindow = uic.loadUiType("team_editor.ui")


class TeamEditor(QtBaseWindow, UI_MainWindow):
    def __init__(self, team=None, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        if team:
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
        pass

    def edit_member_clicked(self):
        pass

    def delete_member_clicked(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TeamEditor(Team(1200, "smashers"))
    window.show()
    sys.exit(app.exec_())
