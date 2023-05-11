import configparser
import sys
import types

from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog
import database
from database import User
from ui.ui_main import Ui_MainWindow



class LoginScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        database.global_init()
        self.session = database.create_session()
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_sigh_in.clicked.connect(self.sing_in)

    def login(self):
        login = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        get_login = self.session.query(User).filter(User.username == str(login)).first()
        # users = self.session.query(User).all()
        # print(type(get_login))
        # for i in users:
        #     print(i)
        if isinstance(get_login, User):
            if password == get_login.password.strip():
                print('yes')
            else:
                print('no')

    def sing_in(self):
        pass

    def test(self):
        print(1)


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
