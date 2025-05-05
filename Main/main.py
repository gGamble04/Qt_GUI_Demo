import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Main.UI.main_window_ui import Ui_mw_Main
from Application_Login.Login import Login_Form
from Persons.add_person import AddPerson

class MainWindow(qtw.QMainWindow, Ui_mw_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_quit.triggered.connect(self.close)
        self.action_addPerson.triggered.connect(self.open_add_person)

        self.form = Login_Form()
        self.form.login_success.connect(self.show)
        self.form.show()

    @qtc.Slot()
    def open_add_person(self):
        self.form = AddPerson()
        self.form.exec()
        
        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    
    window = MainWindow()
    
    sys.exit(app.exec())
