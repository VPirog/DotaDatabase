import configparser
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from database import global_init, create_session
from ui.ui_main import Ui_MainWindow

config = configparser.ConfigParser()
config.read('../config/config.ini')

database_host = config['database']['host']
database_port = config['database']['port']
database_username = config['database']['username']
database_password = config['database']['password']
database_name = config['database']['name']


class LoginScreen(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        global_init(database_host, database_port, database_username, database_password, database_name)
        self.session = create_session()
        # self.pushButton.clicked.connect(self.load_table)
        # self.tableWidget.doubleClicked.connect(self.update_student)
        # self.tableWidget.cellChanged.connect(self.cell_changed)
        # self.pushButton_open_file.clicked.connect(self.color_dialog)


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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginScreen()
    ex.show()
    sys.exit(app.exec())
