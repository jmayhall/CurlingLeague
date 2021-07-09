import sys

from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog

from CurlingLeague.league import League
from CurlingLeague.league_database import LeagueDatabase
from PyQt5 import uic, QtWidgets

UI_MainWindow, QtBaseWindow = uic.loadUiType("main_window.ui")


class MainWindow(QtBaseWindow, UI_MainWindow):
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

    def load_button_clicked(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               ("Open Database"), "../",
                                               ("Database Files (*.dbf)"));

        file = fileName[0]
        if file:
            self.db.load(file)
            self.db = LeagueDatabase.instance()
        self.update_ui()

    def save_button_clicked(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               ("Select Database"), "../",
                                               ("Database Files (*.dbf)"));

        file = fileName[0]
        if file:
            self.db.save(file)
            dialog = QMessageBox(QMessageBox.Icon.Information,
                                 "Save Confirmation",
                                 "League database has been saved!",
                                 QMessageBox.StandardButton.Ok)
            result = dialog.exec()
        self.update_ui()



    def add_league_clicked(self):
        league_name = self.new_league_lineedit.text()
        leag = League(self.db.next_oid(), league_name)
        self.db.add_league(leag)
        self.update_ui()
        self.new_league_lineedit.clear()

    def edit_league_clicked(self):
        pass

    def delete_league_clicked(self):
        dialog = QMessageBox(QMessageBox.Icon.Information,
                             "Confirm Delete",
                             "The selected league will be deleted!",
                             QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        result = dialog.exec()
        if result == QMessageBox.StandardButton.Ok:
            print("Approved")

    def import_league_clicked(self):
        league_name = self.import_league_lineedit.text()
        if league_name != "":
            fileName = QFileDialog.getOpenFileName(self,
                                                    ("Open League File"), "../",
                                                    ("Teams Files (*.csv *.txt)"));

            file = fileName[0]
            self.db.import_league(league_name, file)
            self.update_ui()
            self.import_league_lineedit.clear()

    def export_league_clicked(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
