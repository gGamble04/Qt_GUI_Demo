import sys
from pathlib import Path
from PySide6 import QtCore as qtc, QtWidgets as qtw, QtGui as qtg
import pandas as pd
from pathlib import Path 

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from View_People.UI.View_Persons_ui import Ui_veiw_people_form

class ViewPeople(qtw.QWidget, Ui_veiw_people_form):
    """
    This is the view people window of the application.
    This window displays a table of persons data loaded from a CSV file.
    It allows the user to search for specific persons using a search bar.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Path to csv with persons data
        self.persons_data_path = Path(__file__).resolve().parent.parent / "Persons_Data.csv"
        
        # Function to load CSV data into the table
        self.load_csv_to_table()

        # Function to filter the table based on the search input
        self.le_search.textChanged.connect(self.filter_table)

    def load_csv_to_table(self):
        """
        Load the CSV data into the table widget.
        """
        persons_data = pd.read_csv(self.persons_data_path)

        model = qtg.QStandardItemModel(persons_data.shape[0], persons_data.shape[1])
        model.setHorizontalHeaderLabels(persons_data.columns)

        # Fill NaN values with N/A
        persons_data.fillna("N/A", inplace=True)  

        # Remove trailing zeros from phone numbers
        if "Phone Number" in persons_data.columns:
            persons_data["Phone Number"] = persons_data["Phone Number"].astype(str).str.replace(r'\.0$', '', regex=True)

        for row in range(persons_data.shape[0]):
            for column in range(persons_data.shape[1]):
                item = qtg.QStandardItem(str(persons_data.iat[row, column]))
                model.setItem(row, column, item)

        self.view_people_table.setModel(model)
        self.view_people_table.horizontalHeader().setSectionResizeMode(qtw.QHeaderView.Stretch)
        self._model= model

    def filter_table(self, text):
        text = text.lower()
        for row in range(self._model.rowCount()):
            match = False
            for col in range(self._model.columnCount()):
                item = self._model.item(row, col)
                if text in item.text().lower():
                    match = True
                    break
            self.view_people_table.setRowHidden(row, not match)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = ViewPeople()
    window.show()
    sys.exit(app.exec())