import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Persons.UI.add_person_window_ui import Ui_d_Person

class AddPerson(qtw.QDialog, Ui_d_Person):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gb_Person.setTitle("Add Person")
        self.lb_message.setText("Add a new person to the database")

        # Buttons (Accept and Reject)
        self.pb_close.clicked.connect(self.reject)# <<<
        self.pb_submit.clicked.connect(self.process_entry)

    @qtc.Slot()
    def process_entry(self):

        self.lb_message.setText("New Person Added")
        self.le_first_name.clear()
        self.le_last_name.clear()

        self.le_first_name.setFocus()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = AddPerson()
    form.open()
    sys.exit(app.exec())