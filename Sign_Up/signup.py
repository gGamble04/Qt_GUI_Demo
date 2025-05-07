import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg
import pandas as pd

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Sign_Up.UI.Sign_Up_Window_ui import Ui_W_Signup_Form

class Sign_Up_Form(qtw.QWidget, Ui_W_Signup_Form):
    """
    This is the signup window of the application.
    This window prompts the user for a User ID and Password.
    It checks the entered credentials against a CSV file containing user data.
    If the credentials are valid, it adds the new user to the CSV file.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Path to csv with user data
        self.user_info_path = Path(__file__).resolve().parent.parent / "UserID_Passwords.csv"

        # Connect the buttons to their respective slots
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_signup)

    @qtc.Slot()
    def process_signup(self):
        """
        Process the signup when the OK button is clicked.
        This is a placeholder for actual signup logic.
        """
        user_id = self.le_UserID.text().strip()
        password = self.le_Password.text().strip()
        retype_password = self.le_retype_password.text().strip()

        # Check if any field is empty
        if not user_id or not password or not retype_password:
            self.lb_message.setText("Please fill in all fields.")
            return
        
        # Check if the passwords match
        if password != retype_password:
            self.lb_message.setText("Passwords do not match.")
            self.le_Password.clear()
            self.le_retype_password.clear()
            return
        
        # Load existing user data
        self.user_info = pd.read_csv(self.user_info_path)
        
        # Check if the user ID already exists
        if user_id in self.user_info["User ID"].values:
            self.lb_message.setText("User ID already exists.")
            self.le_UserID.clear()
            return
        
        # Add the new user ID and password to the DataFrame
        self.user_info.loc[len(self.user_info)] = [user_id, password]
        self.user_info.to_csv(self.user_info_path, index=False)
        self.lb_message.setText("Singup successful!")
        qtc.QTimer.singleShot(1500, self.close) # Close the window after 1.5 seconds
  
        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Sign_Up_Form()
    window.show()
    sys.exit(app.exec())
        