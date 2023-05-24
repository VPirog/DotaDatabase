import configparser
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox, QDialog
import database
from database import User
from ui.ui_register import Ui_Dialog


class Registration(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        database.global_init()
        self.session = database.create_session()
        self.pushButton_complite.clicked.connect(self.sing_in)

    def sing_in(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        country = self.comboBox.currentText()
        user = User(username=username,
                    password=password,
                    country=country)
        get_login = self.session.query(User).filter(User.username == str(username).strip()).first()
        print(get_login)
        success = isinstance(username, str) and isinstance(password,
                                                           str) and username != '' and password != '' and get_login is None
        if success:
            self.session.add(user)
            self.session.commit()
            self.close()
        elif get_login is not None:
            QMessageBox.critical(self,
                                 "Error",
                                 'This Login Exist',
                                 QMessageBox.Retry)

        else:
            QMessageBox.critical(self,
                                 "Error",
                                 'Information wrong format! \nTry Login and Password as string',
                                 QMessageBox.Retry)


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook
