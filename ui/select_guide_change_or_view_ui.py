import configparser
import sys
import types

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QDialog, QLineEdit, QTableWidgetItem

import database
from database import Guide, global_init, create_session, Hero, UserRating, GuideCommentary, User

from .select_guide import Ui_Dialog


class SelectGuideChangeOrView(QDialog, Ui_Dialog):

    def __init__(self, login_structure, old_window, guide_structure):
        super().__init__()
        self.setupUi(self)
        old_window.close()
        self.login_structure = login_structure
        self.guide_structure = guide_structure
        self.session = create_session()
        self.old_guide = self.session.query(Guide).get(self.guide_structure.id)
        print(self.old_guide)
        self.initUI()

    def initUI(self):
        database.global_init()
        self.zapolnit_govno()
        self.quitButton.clicked.connect(self.quit)
        self.saveButton.clicked.connect(self.save)

    def save(self):
        if self.login_structure.id == self.guide_structure.owner_user.id:
            self.old_guide.name = self.tableWidget.item(0, 0).text()
            self.old_guide.description = self.tableWidget.item(3, 0).text()
            self.old_guide.main_text = self.tableWidget.item(4, 0).text()

            self.session.commit()

            from ui import GuideView
            self.tableWidget = GuideView(self.login_structure, self)
            self.tableWidget.exec_()
        else:
            session = create_session()
            rating = self.tableWidget.item(2, 0).text()
            rate = UserRating(
                user_id=self.login_structure.id,
                guide_id=self.guide_structure.id,
                rating=rating
            )
            # TODO: Удалять старую оценку и создавать новую оценку ВСЕГДА и тогда обновлять рейтинг всех(?) гайдов
            session.add(rate)
            session.commit()

            from ui import GuideView
            self.tableWidget = GuideView(self.login_structure, self)
            self.tableWidget.exec_()

    def quit(self):
        from ui import GuideView
        self.tableWidget = GuideView(self.login_structure, self)
        self.tableWidget.exec_()

    def zapolnit_govno(self):
        item = QTableWidgetItem()
        item.setText(self.guide_structure.name)
        self.tableWidget.setItem(0, 0, item)
        item = QTableWidgetItem()
        item.setText(self.guide_structure.hero.name)
        self.tableWidget.setItem(1, 0, item)
        item = QTableWidgetItem()
        item.setText(self.guide_structure.name)
        self.tableWidget.setItem(2, 0, item)
        item = QTableWidgetItem()
        item.setText(self.guide_structure.description)
        self.tableWidget.setItem(3, 0, item)
        item = QTableWidgetItem()
        item.setText(self.guide_structure.main_text)
        self.tableWidget.setItem(4, 0, item)

        session = create_session()
        tmp = session.query(GuideCommentary).filter(GuideCommentary.guide_id == self.guide_structure.id).all()
        print(tmp, type(tmp))
        for row_pos, commentary_i in enumerate(tmp, start=6):
            self.tableWidget.insertRow(row_pos)
            item = QTableWidgetItem()
            item.setText(session.query(User).filter(User.id == commentary_i.user_id).first().username.strip())
            self.tableWidget.setVerticalHeaderItem(row_pos, item)
            item = QTableWidgetItem()
            item.setText(commentary_i.commentary)
            self.tableWidget.setItem(row_pos, 0, item)


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
