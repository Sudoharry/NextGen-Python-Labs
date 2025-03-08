from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QVBoxLayout, 
                             QPushButton, QWidget, QLineEdit, QTableWidget,
                             QTableWidgetItem, QHBoxLayout, QMessageBox,
                             QHeaderView, QDateEdit, QComboBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDate
import sys
import os
import json

basedir = os.path.dirname(__file__)
DATA_FILE = os.path.join(basedir, 'motor_data.json')

class MotorSurveyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motor Survey Reporting System")
        self.setMinimumSize(800, 600)
        
        # Initialize data storage
        self.motor_data = []
        self.load_data()
        
        # Create UI elements
        self.create_widgets()
        self.create_layout()
        self.setup_table()
        self.show()

    def create_widgets(self):
        """Create input widgets"""
        self.motor_id_input = QLineEdit(placeholderText="Motor ID")
        self.motor_type_input = QComboBox()
        self.motor_type_input.addItems(["AC Induction", "DC Brushless", "Stepper", "Servo"])
        self.power_rating_input = QLineEdit(placeholderText="Power Rating (kW)")
        self.installation_date = QDateEdit(calendarPopup=True)
        self.installation_date.setDate(QDate.currentDate())
        self.location_input = QLineEdit(placeholderText="Location")
        self.status_input = QComboBox()
        self.status_input.addItems(["Operational", "Maintenance", "Faulty"])
        
        # Buttons
        self.add_btn = QPushButton("Add Motor", clicked=self.add_motor)
        self.edit_btn = QPushButton("Edit Selected", clicked=self.edit_motor)
        self.delete_btn = QPushButton("Delete Selected", clicked=self.delete_motor)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Motor ID", "Type", "Power (kW)", "Installation Date", 
            "Location", "Status"
        ])

    def create_layout(self):
        """Set up main layout"""
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        
        # Input form layout
        form_layout = QVBoxLayout()
        inputs = [
            self.motor_id_input,
            self.motor_type_input,
            self.power_rating_input,
            self.installation_date,
            self.location_input,
            self.status_input,
            self.add_btn,
            self.edit_btn,
            self.delete_btn
        ]
        
        for widget in inputs:
            form_layout.addWidget(widget)
        
        # Add layouts to main layout
        main_layout.addLayout(form_layout, 1)
        main_layout.addWidget(self.table, 3)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def setup_table(self):
        """Configure table appearance"""
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.populate_table()

    def load_data(self):
        """Load data from JSON file"""
        try:
            with open(DATA_FILE, 'r') as f:
                self.motor_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.motor_data = []

    def save_data(self):
        """Save data to JSON file"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.motor_data, f, indent=2)

    def populate_table(self):
        """Refresh table with current data"""
        self.table.setRowCount(len(self.motor_data))
        for row, motor in enumerate(self.motor_data):
            self.table.setItem(row, 0, QTableWidgetItem(motor['motor_id']))
            self.table.setItem(row, 1, QTableWidgetItem(motor['motor_type']))
            self.table.setItem(row, 2, QTableWidgetItem(str(motor['power_rating'])))
            self.table.setItem(row, 3, QTableWidgetItem(motor['installation_date']))
            self.table.setItem(row, 4, QTableWidgetItem(motor['location']))
            self.table.setItem(row, 5, QTableWidgetItem(motor['status']))

    def validate_inputs(self):
        """Check required fields are filled"""
        if not self.motor_id_input.text().strip():
            QMessageBox.warning(self, "Error", "Motor ID is required!")
            return False
        try:
            float(self.power_rating_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid power rating!")
            return False
        return True

    def clear_inputs(self):
        """Reset input fields"""
        self.motor_id_input.clear()
        self.motor_type_input.setCurrentIndex(0)
        self.power_rating_input.clear()
        self.installation_date.setDate(QDate.currentDate())
        self.location_input.clear()
        self.status_input.setCurrentIndex(0)

    def add_motor(self):
        """Add new motor entry"""
        if not self.validate_inputs():
            return
        
        new_motor = {
            "motor_id": self.motor_id_input.text(),
            "motor_type": self.motor_type_input.currentText(),
            "power_rating": float(self.power_rating_input.text()),
            "installation_date": self.installation_date.date().toString("yyyy-MM-dd"),
            "location": self.location_input.text(),
            "status": self.status_input.currentText()
        }
        
        self.motor_data.append(new_motor)
        self.save_data()
        self.populate_table()
        self.clear_inputs()
        QMessageBox.information(self, "Success", "Motor added successfully!")

    def edit_motor(self):
        """Edit selected motor entry"""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a motor to edit!")
            return
        
        if not self.validate_inputs():
            return
        
        updated_motor = {
            "motor_id": self.motor_id_input.text(),
            "motor_type": self.motor_type_input.currentText(),
            "power_rating": float(self.power_rating_input.text()),
            "installation_date": self.installation_date.date().toString("yyyy-MM-dd"),
            "location": self.location_input.text(),
            "status": self.status_input.currentText()
        }
        
        self.motor_data[selected_row] = updated_motor
        self.save_data()
        self.populate_table()
        QMessageBox.information(self, "Success", "Motor updated successfully!")

    def delete_motor(self):
        """Delete selected motor entry"""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select a motor to delete!")
            return
        
        reply = QMessageBox.question(
            self, 'Confirm Delete',
            'Are you sure you want to delete this motor entry?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            del self.motor_data[selected_row]
            self.save_data()
            self.populate_table()
            QMessageBox.information(self, "Success", "Motor deleted successfully!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "report.svg")))
    window = MotorSurveyApp()
    sys.exit(app.exec_())