import sys
import os
import json
import sqlite3
import pandas as pd
from datetime import datetime
from hashlib import sha256
from reportlab.pdfgen import canvas
from PyQt5.QtCore import Qt, QDate, QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QDialog, QDialogButtonBox, QLabel, QVBoxLayout,
    QPushButton, QWidget, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout,
    QMessageBox, QHeaderView, QDateEdit, QComboBox, QFileDialog, QAction
)

# Configuration
basedir = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(basedir, 'motor_survey.db')
DATA_FILE = os.path.join(basedir, 'motor_data.json')

# Create data file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

class AuthDialog(QDialog):
    """User authentication dialog"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 150)
        
        layout = QVBoxLayout()
        self.username = QLineEdit(placeholderText="Username")
        self.password = QLineEdit(placeholderText="Password", echoMode=QLineEdit.Password)
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.username)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password)
        layout.addWidget(buttons)
        self.setLayout(layout)
        
        buttons.accepted.connect(self.authenticate)
        buttons.rejected.connect(self.reject)

    def authenticate(self):
        """Verify user credentials with error handling"""
        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT password, salt FROM users WHERE username=?', 
                             (self.username.text(),))
                result = cursor.fetchone()
                
            if result and sha256((self.password.text() + result[1]).encode()).hexdigest() == result[0]:
                self.accept()
            else:
                QMessageBox.warning(self, "Error", "Invalid username or password")
        except sqlite3.OperationalError:
            QMessageBox.critical(self, "Database Error", 
                                "Database not initialized!\nRun setup_db.py first")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Authentication failed: {str(e)}")

class MotorSurveyApp(QMainWindow):
    """Main application window"""
    def __init__(self, username):
        super().__init__()
        self.current_user = username
        self.motor_data = []
        
        # Initialize components
        self.setWindowTitle(f"Motor Survey - {username}")
        self.setMinimumSize(1000, 700)
        self.load_data()
        self.init_ui()
        self.init_db()
        self.setup_menu()
        self.show()

    def init_ui(self):
        """Initialize user interface components"""
        # Input widgets
        self.motor_id_input = QLineEdit(placeholderText="Motor ID")
        self.motor_type = QComboBox()
        self.motor_type.addItems(["AC Induction", "DC Brushless", "Stepper", "Servo"])
        self.power_input = QLineEdit(placeholderText="Power (kW)")
        self.install_date = QDateEdit(calendarPopup=True)
        self.install_date.setDate(QDate.currentDate())
        self.location_input = QLineEdit(placeholderText="Location")
        self.status = QComboBox()
        self.status.addItems(["Operational", "Maintenance", "Faulty"])
        
        # Action buttons
        self.add_btn = QPushButton("Add Motor", clicked=self.add_motor)
        self.edit_btn = QPushButton("Edit Selected", clicked=self.edit_motor)
        self.del_btn = QPushButton("Delete Selected", clicked=self.delete_motor)
        
        # Data table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "ID", "Type", "Power (kW)", "Install Date", "Location", "Status"
        ])
        self.setup_table()
        
        # Search/filter
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit(placeholderText="Search...")
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["All", "Operational", "Maintenance", "Faulty"])
        
        # Main layout
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        form_layout = QVBoxLayout()
        
        # Assemble UI components
        for widget in [self.motor_id_input, self.motor_type, self.power_input,
                      self.install_date, self.location_input, self.status,
                      self.add_btn, self.edit_btn, self.del_btn]:
            form_layout.addWidget(widget)
        
        search_layout.addWidget(QLabel("Filter:"))
        search_layout.addWidget(self.filter_combo)
        search_layout.addWidget(self.search_input)
        
        main_layout.addLayout(form_layout, 1)
        main_layout.addWidget(self.table, 3)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
        # Connect signals
        self.search_input.textChanged.connect(self.filter_data)
        self.filter_combo.currentIndexChanged.connect(self.filter_data)

    def setup_table(self):
        """Configure table appearance and behavior"""
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.populate_table()

    def load_data(self):
        """Load motor data from JSON file"""
        try:
            with open(DATA_FILE, 'r') as f:
                self.motor_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.motor_data = []

    def save_data(self):
        """Save motor data to JSON file"""
        with open(DATA_FILE, 'w') as f:
            json.dump(self.motor_data, f, indent=2)

    def populate_table(self, data=None):
        """Refresh table with provided data"""
        data = data or self.motor_data
        self.table.setRowCount(len(data))
        for row, motor in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(motor['motor_id']))
            self.table.setItem(row, 1, QTableWidgetItem(motor['motor_type']))
            self.table.setItem(row, 2, QTableWidgetItem(str(motor['power_rating'])))
            self.table.setItem(row, 3, QTableWidgetItem(motor['installation_date']))
            self.table.setItem(row, 4, QTableWidgetItem(motor['location']))
            self.table.setItem(row, 5, QTableWidgetItem(motor['status']))

    def filter_data(self):
        """Filter table data based on search and status"""
        search_text = self.search_input.text().lower()
        status_filter = self.filter_combo.currentText()
        
        filtered_data = [
            motor for motor in self.motor_data
            if (search_text in motor['motor_id'].lower() or 
                search_text in motor['location'].lower()) and
               (status_filter == "All" or motor['status'] == status_filter)
        ]
        self.populate_table(filtered_data)

    def init_db(self):
        """Initialize database connection and tables"""
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                salt TEXT
            )''')
            conn.execute('''CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                user TEXT,
                action TEXT,
                timestamp DATETIME,
                details TEXT
            )''')

    def setup_menu(self):
        """Create application menu system"""
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu("&File")
        export_pdf = QAction("Export to PDF", self)
        export_excel = QAction("Export to Excel", self)
        file_menu.addActions([export_pdf, export_excel])
        
        # Admin menu
        admin_menu = menu_bar.addMenu("&Admin")
        manage_users = QAction("Manage Users", self)
        change_pass = QAction("Change Password", self)
        view_history = QAction("Audit Log", self)
        admin_menu.addActions([manage_users, change_pass, view_history])
        
        # Connect actions
        export_pdf.triggered.connect(self.export_pdf)
        export_excel.triggered.connect(self.export_excel)
        manage_users.triggered.connect(self.manage_users)
        change_pass.triggered.connect(self.change_password)
        view_history.triggered.connect(self.view_history)

    def export_pdf(self):
        """Generate PDF report"""
        path, _ = QFileDialog.getSaveFileName(self, "Save PDF", "", "PDF Files (*.pdf)")
        if not path:
            return
        
        pdf = canvas.Canvas(path)
        pdf.setTitle("Motor Survey Report")
        pdf.setFont("Helvetica", 12)
        
        # Header
        pdf.drawString(50, 800, f"Motor Survey Report ({datetime.now().strftime('%Y-%m-%d')})")
        pdf.line(50, 795, 550, 795)
        
        # Content
        y = 750
        for idx, motor in enumerate(self.motor_data, 1):
            text = (f"{idx}. {motor['motor_id']} - {motor['motor_type']} "
                   f"({motor['power_rating']}kW) - {motor['status']}")
            pdf.drawString(50, y, text)
            y -= 20
            if y < 50:
                pdf.showPage()
                y = 800
        
        pdf.save()
        self._log_action("EXPORT_PDF", f"Exported {len(self.motor_data)} records")

    def export_excel(self):
        """Export data to Excel format"""
        path, _ = QFileDialog.getSaveFileName(self, "Save Excel", "", "Excel Files (*.xlsx)")
        if path:
            pd.DataFrame(self.motor_data).to_excel(path, index=False)
            self._log_action("EXPORT_EXCEL", f"Exported {len(self.motor_data)} records")

    def manage_users(self):
        """Show user management dialog"""
        if not self._is_admin():
            QMessageBox.warning(self, "Access Denied", "Admin privileges required!")
            return
        
        dialog = UserDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self._create_user(
                dialog.username.text(), 
                dialog.password.text()
            )

    def change_password(self):
        """Show password change dialog"""
        dialog = PasswordDialog(self.current_user)
        if dialog.exec_() == QDialog.Accepted:
            self._update_password(
                self.current_user,
                dialog.old_password.text(),
                dialog.new_password.text()
            )

    def view_history(self):
        """Display audit log history"""
        with sqlite3.connect(DB_FILE) as conn:
            history = conn.execute('''SELECT * FROM history 
                                    ORDER BY timestamp DESC LIMIT 100''').fetchall()
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Audit History")
        dialog.resize(600, 400)
        
        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["User", "Action", "Timestamp", "Details"])
        table.setRowCount(len(history))
        
        for row, record in enumerate(history):
            table.setItem(row, 0, QTableWidgetItem(record[1]))
            table.setItem(row, 1, QTableWidgetItem(record[2]))
            table.setItem(row, 2, QTableWidgetItem(record[3]))
            table.setItem(row, 3, QTableWidgetItem(record[4]))
        
        layout = QVBoxLayout()
        layout.addWidget(table)
        dialog.setLayout(layout)
        dialog.exec_()

    def _is_admin(self):
        """Check if current user is admin"""
        return self.current_user.lower() == "admin"

    def _create_user(self, username, password):
        """Create new user account"""
        try:
            self._create_user_db(username, password)
            QMessageBox.information(self, "Success", "User created successfully!")
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Error", "Username already exists!")

    def _create_user_db(self, username, password):
        """Database operation for user creation"""
        salt = os.urandom(16).hex()
        hashed = sha256((password + salt).encode()).hexdigest()
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('''INSERT INTO users (username, password, salt)
                         VALUES (?, ?, ?)''', (username, hashed, salt))

    def _update_password(self, username, old_password, new_password):
        """Update user password"""
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT password, salt FROM users WHERE username=?', (username,))
            result = cursor.fetchone()
            
            if not result:
                QMessageBox.warning(self, "Error", "User not found!")
                return
                
            stored_hash, salt = result
            input_hash = sha256((old_password + salt).encode()).hexdigest()
            
            if input_hash != stored_hash:
                QMessageBox.warning(self, "Error", "Current password is incorrect!")
                return
            
            new_salt = os.urandom(16).hex()
            new_hash = sha256((new_password + new_salt).encode()).hexdigest()
            
            cursor.execute('''UPDATE users SET 
                           password=?, salt=?
                           WHERE username=?''',
                           (new_hash, new_salt, username))
            conn.commit()
            
        QMessageBox.information(self, "Success", "Password updated successfully!")

    def _log_action(self, action, details):
        """Log user actions to database"""
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute('''INSERT INTO history (user, action, timestamp, details)
                         VALUES (?, ?, ?, ?)''',
                         (self.current_user, action, datetime.now(), details))

    # Motor management methods
    def add_motor(self):
        """Add new motor entry"""
        if not self.validate_inputs():
            return
        
        new_motor = {
            "motor_id": self.motor_id_input.text(),
            "motor_type": self.motor_type.currentText(),
            "power_rating": float(self.power_input.text()),
            "installation_date": self.install_date.date().toString("yyyy-MM-dd"),
            "location": self.location_input.text(),
            "status": self.status.currentText()
        }
        
        self.motor_data.append(new_motor)
        self.save_data()
        self.populate_table()
        self.clear_inputs()
        self._log_action("ADD", f"Added motor {new_motor['motor_id']}")
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
            "motor_type": self.motor_type.currentText(),
            "power_rating": float(self.power_input.text()),
            "installation_date": self.install_date.date().toString("yyyy-MM-dd"),
            "location": self.location_input.text(),
            "status": self.status.currentText()
        }
        
        self.motor_data[selected_row] = updated_motor
        self.save_data()
        self.populate_table()
        self._log_action("EDIT", f"Updated motor {updated_motor['motor_id']}")
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
            motor_id = self.motor_data[selected_row]['motor_id']
            del self.motor_data[selected_row]
            self.save_data()
            self.populate_table()
            self._log_action("DELETE", f"Deleted motor {motor_id}")
            QMessageBox.information(self, "Success", "Motor deleted successfully!")

    def validate_inputs(self):
        """Validate required fields"""
        if not self.motor_id_input.text().strip():
            QMessageBox.warning(self, "Error", "Motor ID is required!")
            return False
        try:
            float(self.power_input.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Invalid power rating!")
            return False
        return True

    def clear_inputs(self):
        """Clear input fields"""
        self.motor_id_input.clear()
        self.motor_type.setCurrentIndex(0)
        self.power_input.clear()
        self.install_date.setDate(QDate.currentDate())
        self.location_input.clear()
        self.status.setCurrentIndex(0)
def initialize_system():
    """First-run system initialization"""
    try:
        with sqlite3.connect(DB_FILE) as conn:
            # Create tables
            conn.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT,
                salt TEXT
            )''')
            conn.execute('''CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                user TEXT,
                action TEXT,
                timestamp DATETIME,
                details TEXT
            )''')
            
            # Create default admin if not exists
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users WHERE username='admin'")
            if cursor.fetchone()[0] == 0:
                salt = os.urandom(16).hex()
                password = 'admin123'
                hashed = sha256((password + salt).encode()).hexdigest()
                conn.execute('''INSERT INTO users 
                             (username, password, salt)
                             VALUES (?, ?, ?)''',
                             ('admin', hashed, salt))
    except Exception as e:
        print(f"Initialization failed: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    # Initialize system components
    initialize_system()
    
    # Start application
    QThread.currentThread()  # Initialize main thread
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(basedir, "icons", "engine-motor-svgrepo-com.svg")))
    
    # Show login dialog
    login_dialog = AuthDialog()
    if login_dialog.exec_() == QDialog.Accepted:
        window = MotorSurveyApp(login_dialog.username.text())
        sys.exit(app.exec_())
    app.quit()