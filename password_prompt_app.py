import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class PasswordPrompt(QMainWindow):
    def __init__(self, correct_password):
        super().__init__()
        self.correct_password = correct_password
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Password Prompt")
        self.setGeometry(300, 300, 400, 150)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.label = QLabel("Enter the password:", self)
        self.layout.addWidget(self.label)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.button = QPushButton("Submit", self)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.check_password)

    def check_password(self):
        entered_password = self.password_input.text()
        if entered_password == self.correct_password:
            self.hide()  # Hide the password prompt window
            self.open_browser()
        else:
            self.show_message("Incorrect Password", "Please enter the correct password and try again.")

    def open_browser(self):
        # Open Chrome browser here
        import subprocess
        subprocess.Popen(["C:\Program Files\Google\Chrome\Application\chrome.exe", "https://example.com"])

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    correct_password = "piyush"
    window = PasswordPrompt(correct_password)
    window.show()
    sys.exit(app.exec_())
