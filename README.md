### Author

Jeff Mayhall - Auburn University
July 11, 2021

### Features

- Supports loading and saving a database file to local storage containing all Curling League Teams, Competitions and Members.
- Supports importing league data from csv files

### Usage
- A simple graphical interface for managing a Curling League Database that allows saving the database file to local storage.  
- Leagues contain team and competition information.
- Teams contain team member information.  
- Leagues, Teams and Members can be edited and updated as needed, but the database must be manually saved after any changes.

**Running the application** 

The application is accessed by running 'main_window.py' from CurlingLeague/GUI, or if the setup.py is installed, can be run using the console script 'main'.  The GUI will launch and all features are accessible from this main window.

**Source Code**
[Github Project - CurlingLeague](https://github.com/jmayhall/CurlingLeague)

**File Formats**
- CSV files must be comma deliminated and UTF-8 format

**Required Python Packages**
- yagmail
- PyQt5
- pyqt5_tools
- keyring
