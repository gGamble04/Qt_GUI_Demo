import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg
import pandas as pd

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Application_Login.UI.Login_Window_ui import Ui_W_Login_Form
from Sign_Up.signup import Sign_Up_Form

class Login_Form(qtw.QWidget, Ui_W_Login_Form):
    """
    This is the login window of the application.
    This window prompts the user for their User ID and Password.
    It checks the entered credentials against a CSV file containing user data.
    If the credentials are valid, it emits a signal indicating successful login.
    If the credentials are invalid, it displays an error message.
    It also provides a button to open a signup form for new users.
    """
    # Signal to indicate successful login
    login_success = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Path to csv with user data
        self.user_info_path = Path(__file__).resolve().parent.parent / "UserID_Passwords.csv"

        # Connect the buttons to their respective slots
        self.pb_cancel.clicked.connect(self.close)

        self.pb_ok.clicked.connect(self.process_login)

        self.clb_signup.clicked.connect(self.open_signup)

    @qtc.Slot()
    def process_login(self):
        """Processes the login credentials."""

        user_id = self.le_UserID.text().strip()
        password = self.le_Password.text().strip()

        if not user_id or not password:
            self.lb_message.setText("Please fill in all fields.")
            return
        
        self.user_info = pd.read_csv(self.user_info_path)
        if user_id in self.user_info["User ID"].values and password in self.user_info["Password"].values:
            self.lb_message.setText("Login successful!")
            self.le_UserID.clear()
            self.le_Password.clear()
            self.le_UserID.setFocus()

            # Emit the login_success signal
            self.login_success.emit()

            # Close the login form
            self.close()
        

        else:
            self.lb_message.setText("Invalid username or password.")

    @qtc.Slot()
    def open_signup(self):
        """Opens the signup form."""

        self.form = Sign_Up_Form()
        self.form.show()

        # Clear the input fields after signup
        self.le_UserID.clear()
        self.le_Password.clear()
        self.le_UserID.setFocus()
   
    
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Login_Form()
    window.show()
    sys.exit(app.exec())

