from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QApplication, QTextBrowser, QMessageBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.setFixedSize(385, 429)
        uic.loadUi('form.ui',self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stylish Login System')
        self.login_btn.clicked.connect(self.check)
       
        
    def check(self):
        username_text = self.username_entry.text()
        password_text = self.password_entry.text()
        if username_text == 'Celestine' and password_text == 'squid1.0':
            self.message = QMessageBox()
            self.message.setWindowTitle('Success')
            self.message.setText("""
Account Login Successful.
Thank You For enrolling in our community  
            """)
            self.message.setInformativeText("""
            User Details
                Username: Celestine
                Password: squid 1.0 

            """)
            self.message.setIcon(QMessageBox.Information)
            self.message.buttonClicked.connect(self.clear)
            self.message.exec_()
        else:
            self.message = QMessageBox()
            self.message.setWindowTitle('Failed')
            self.message.setText("""
Account Registration Failed...
Account Does Not Exist...
            """)
            self.message.setStandardButtons(QMessageBox.Ignore)
            self.message.setDefaultButton(QMessageBox.Ignore)
            self.message.setInformativeText(f"""
            The only account that matches that account is:
                Username: {username_text}
                Password: ******** 

            """)
            self.message.setIcon(QMessageBox.Warning)
            self.message.buttonClicked.connect(self.clear)
            self.message.exec_()   
    
    def clear(self):
        self.username_entry.setText('')
        self.password_entry.setText('')

    
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec_())

