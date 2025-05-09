import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg
import pandas as pd
import re

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from Persons.UI.add_person_window_ui import Ui_d_Person

class AddPerson(qtw.QDialog, Ui_d_Person):
    """
    This is the add person window of the application.
    This window prompts the user for a first name, last name, email, and phone number.
    It checks the entered data against a CSV file containing person data.
    If the data is valid, it adds the new person to the CSV file.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Path to csv with persons data
        self.persons_data_path = Path(__file__).resolve().parent.parent / "Persons_Data.csv"

        self.gb_Person.setTitle("Add Person")
        self.lb_message.setText("Add a new person to the database")

        # Buttons (Reject)
        self.pb_close.clicked.connect(self.reject)# <<<
        
        # Connects the submit button to the process_entry method
        self.pb_submit.clicked.connect(self.process_entry)

        self.le_first_name.setFocus()

    @qtc.Slot()
    def process_entry(self):
        """Processes the entry of a new person."""

        first_name = self.le_first_name.text().strip()
        last_name = self.le_last_name.text().strip()
        email = self.le_email.text().strip()
        phone = self.le_phoneNumber.text().strip()

        # Check if first and last names fields are empty
        if not first_name and not last_name:
            self.lb_message.setText("Please fill in all fields.")
            self.le_first_name.setFocus()
            return

        if not first_name:
            self.lb_message.setText("First name is required.")
            self.le_first_name.setFocus()
            return
        
        if not last_name:
            self.lb_message.setText("Last name is required.")
            self.le_last_name.setFocus()
            return
        
        # Check if fields are valid
        if not first_name.isalpha():
            self.lb_message.setText("First name must contain only letters.")
            self.le_first_name.clear()
            self.le_first_name.setFocus()
            return
        
        if not last_name.isalpha():
            self.lb_message.setText("Last name must contain only letters.")
            self.le_last_name.clear()
            self.le_last_name.setFocus()
            return
        
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if email and not re.match(email_regex, email):
            self.lb_message.setText("Invalid email format.")
            self.le_email.clear()
            self.le_email.setFocus()
            return
        
        if phone and not phone.isdigit():
            self.lb_message.setText("Phone number must contain only digits.")
            self.le_phoneNumber.clear()
            self.le_phoneNumber.setFocus()
            return
        
        if phone and len(phone) != 10:
            self.lb_message.setText("Phone number must be 10 digits long.")
            self.le_phoneNumber.clear()
            self.le_phoneNumber.setFocus()
            return
        
        # Load existing persons data
        self.persons_data = pd.read_csv(self.persons_data_path)
        
        """
        Future feature: Check if the person already exists and ask if they still want to add them

        # Check if the person already exists and ask if they still want to add them
        if first_name in self.persons_data["First Name"].values and last_name in self.persons_data["Last Name"].values:
            self.lb_message.setText("Person already exists. Do you want to update their information?")           
            return
        """

        # Add the new user ID and password to the DataFrame
        self.persons_data.loc[len(self.persons_data)] = [first_name, last_name, email, phone]
        self.persons_data.to_csv(self.persons_data_path, index=False)

        ## Clear the input fields
        self.lb_message.setText("New Person Added")
        self.le_first_name.clear()
        self.le_last_name.clear()
        self.le_email.clear()
        self.le_phoneNumber.clear()
        self.le_first_name.setFocus()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    form = AddPerson()
    form.open()
    sys.exit(app.exec())