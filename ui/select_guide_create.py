import configparser
import sys
import types

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QDialog, QLineEdit, QTableWidgetItem

import database
from database import Guide, global_init, create_session, Hero

from .select_guide import Ui_Dialog


class CreateGuide(QDialog, Ui_Dialog):

    def __init__(self, login_structure, old_window):
        super().__init__()
        self.setupUi(self)
        old_window.close()
        self.initUI()
        self.login_structure = login_structure
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
        guide = self.session.query(Guide).first()
        _name = self.tableWidget.item(0, 0).text()
        _hero = self.tableWidget.item(1, 0).text()
        _description = self.tableWidget.item(3, 0).text()
        _main_text = self.tableWidget.item(4, 0).text()
        _hero_id = self.session.query(Hero).filter(Hero.name == str(_hero).strip()).first()

        #
        new_guide = Guide(
            name=_name,
            rating=0.0,
            description=_description,
            main_text=_main_text,
            owner_user_id=self.login_structure.id,
            hero_id=_hero_id.id
        )
        session.add(new_guide)
        session.commit()
        from ui import GuideView

        self.guide_table = GuideView(self.login_structure , self)
        self.guide_table.exec_()

    def quit(self):
        self.close()


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
