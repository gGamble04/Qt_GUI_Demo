import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Application_Login.UI.Login_Window_ui import Ui_W_Login_Form


class Login_Form(qtw.QWidget, Ui_W_Login_Form):

    login_success = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_cancel.clicked.connect(self.close)

        self.pb_ok.clicked.connect(self.process_login)

    @qtc.Slot()
    def process_login(self):
        if self.le_UserID.text() == "Gabe" and self.le_Password.text() == "password":
            self.login_success.emit()
            self.close()

        else:
            self.lb_message.setText("Invalid username or password.")

    
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Login_Form()
    window.show()
    sys.exit(app.exec())

