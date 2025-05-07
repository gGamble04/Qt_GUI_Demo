import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Main.UI.main_window_ui import Ui_mw_Main
from Application_Login.Login import Login_Form
from Persons.add_person import AddPerson
from View_People.view_people import ViewPeople

class MainWindow(qtw.QMainWindow, Ui_mw_Main):
    """
    This is the main window of the application.
    The user is prompted to log in first.
    If the login is successful, the main window is displayed.
    The main window contains a menu bar with options to add a person or view people.
    """
    def __init__(self):
        super().__init__() 

        # Set up the main window
        self.setupUi(self)

        # Connect the quit action to the close method
        self.action_quit.triggered.connect(self.close)

        # Connect the add person action to open_add_person defined below
        self.action_addPerson.triggered.connect(self.open_add_person)

        # Connect the veiw people action to open_view_people defined below
        self.action_viewPeople.triggered.connect(self.open_view_people)

        # set up the login form
        self.form = Login_Form()

        # connect the login success signal to the show method of the main window
        self.form.login_success.connect(self.show)
        self.form.show()

    @qtc.Slot()
    def open_add_person(self):
        """Open the add person form."""
        self.form = AddPerson()
        self.form.exec()
        
    @qtc.Slot()
    def open_view_people(self):
        """Open the view people form."""
        self.form = ViewPeople()
        self.form.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec())
