import sys
from CurlingLeague.league_database import LeagueDatabase
from PyQt5 import uic, QtWidgets

UI_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, UI_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = LeagueDatabase.instance()
        self.load_database_button.clicked.connect(self.load_button_clicked)
        self.save_database_button.clicked.connect(self.save_button_clicked)
        self.add_league_button.clicked.connect(self.add_league_clicked)
        self.edit_league_button.clicked.connect(self.edit_league_clicked)
        self.delete_league_button.clicked.connect(self.delete_league_clicked)
        self.import_league_button.clicked.connect(self.import_league_clicked)
        self.export_league_button.clicked.connect(self.export_league_clicked)

    def load_button_clicked(self):
        pass

    def save_button_clicked(self):
        pass

    def add_league_clicked(self):
        self.db.add_league(self.new_league_lineedit.text(), self.db.next_oid)

    def edit_league_clicked(self):
        pass

    def delete_league_clicked(self):
        pass

    def import_league_clicked(self):
        pass

    def export_league_clicked(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
