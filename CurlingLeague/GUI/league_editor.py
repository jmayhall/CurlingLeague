import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.league import League

from PyQt5 import uic, QtWidgets

UI_MainWindow, QtBaseWindow = uic.loadUiType("league_editor.ui")


class LeagueEditor(QtBaseWindow, UI_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.db = LeagueDatabase.instance()
        self.update_ui()
        self.load_database_button.clicked.connect(self.load_button_clicked)
        self.save_database_button.clicked.connect(self.save_button_clicked)
        self.add_league_button.clicked.connect(self.add_league_clicked)
        self.edit_league_button.clicked.connect(self.edit_league_clicked)
        self.delete_league_button.clicked.connect(self.delete_league_clicked)
        self.import_league_button.clicked.connect(self.import_league_clicked)
        self.export_league_button.clicked.connect(self.export_league_clicked)

    def update_ui(self):
        self.leagues_listwidget.clear()
        for l in self.db.leagues:
            self.leagues_listwidget.addItem(str(l))