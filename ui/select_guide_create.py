import configparser
import sys
import types

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QDialog, QLineEdit

import database
from database import Guide, global_init, create_session, Hero

from .select_guide import Ui_Dialog


class CreateGuide(QDialog, Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        # self.lineEdit_name = QLineEdit()
        # self.lineEdit_hero = QLineEdit()
        # self.lineEdit_description = QLineEdit()
        # self.lineEdit_main_text = QLineEdit()

    def initUI(self):
        database.global_init()
        self.session = database.create_session()
        self.quitButton.clicked.connect(self.quit)
        self.saveButton.clicked.connect(self.save)


    def save(self):
        session = create_session()
        _name = self.tableWidget.verticalHeaderItem(0).text()
        _hero = self.tableWidget.verticalHeaderItem(1).text()
        _description = self.tableWidget.verticalHeaderItem(3).text()
        _main_text = self.tableWidget.verticalHeaderItem(4).text()
        # _hero_id = self.session.query(Hero).filter(Hero.name == _hero).first()
        #
        new_guide = Guide(id=123,
                          name=_name,
                          rating=0.0,
                          description=_description,
                          main_text=_main_text,
                          owner_user_id=1,
                          hero_id=_hero_id.id
                          )
        session.add(new_guide)
        session.commit()



    def quit(self):
        pass











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