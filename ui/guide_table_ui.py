import sys

from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox, QDialog, QTableWidgetItem
import database
from database import User, Guide
from ui.select_guide_change_or_view_ui import SelectGuideChangeOrView
from ui.select_guide_create import CreateGuide
from ui.ui_guide_table import Ui_Dialog


class GuideView(QDialog, Ui_Dialog):
    def __init__(self, login_structure, old_window):
        super().__init__()
        self.setupUi(self)
        old_window.close()
        self.login_structure = login_structure
        self.user_name_label.setText(login_structure.username)
        self.initUI()

    def initUI(self):
        database.global_init()
        self.session = database.create_session()
        self.create_guide_bottom.clicked.connect(self.create_)
        self.load_table()
        self.guide_table.doubleClicked.connect(self.change_or_view_guide)

    def create_(self):
        self.open_create_guide = CreateGuide(self.login_structure, self)
        self.open_create_guide.exec_()

    def load_table(self):
        self.table_is_changeable = False
        guides = self.session.query(Guide).all()
        self.guide_table.setRowCount(0)
        for guide in guides:
            row_position = self.guide_table.rowCount()
            self.guide_table.insertRow(row_position)
            tmp = QTableWidgetItem(str(guide.name))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(guide.hero))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 1, tmp)
            tmp = QTableWidgetItem(str(guide.description))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 2, tmp)
            tmp = QTableWidgetItem(str(guide.rating))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 3, tmp)
        self.table_is_changeable = True

    def change_or_view_guide(self, index: QModelIndex):
        current_row = index.row()
        row_name = self.guide_table.item(current_row, 0).text()
        guide_structure = self.session.query(Guide).filter(Guide.name == str(row_name).strip()).first()
        self.open_change_or_view_guide = SelectGuideChangeOrView(self.login_structure, self, guide_structure)
        self.open_change_or_view_guide.exec_()
        self.load_table()


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
