import sys

from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QMessageBox, QDialog, QTableWidgetItem
import database
from database import User, Guide, Hero, create_session, UserRating
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
        self.load_all()
        self.create_guide_bottom.clicked.connect(self.create_)
        self.search_pushButton.clicked.connect(self.search_by)
        self.guide_table.doubleClicked.connect(self.change_or_view_guide)

    def create_(self):
        self.open_create_guide = CreateGuide(self.login_structure, self)
        self.open_create_guide.exec_()

    def load_all(self):
        self.table_is_changeable = False
        get_guides = self.session.query(Guide).all()
        self.loader(get_guides)

    def loader(self, guides):
        guides.sort()
        self.guide_table.setRowCount(0)
        for guide in guides:
            row_position = self.guide_table.rowCount()
            self.guide_table.insertRow(row_position)
            tmp = QTableWidgetItem()
            hero_name = str(guide.hero).strip()
            # print(hero_name, f":/Hero/raw_hero/{hero_name}.png")
            pixmap = QPixmap(f":/Hero/raw_hero/{hero_name} icon.png").scaled(60, 34)
            tmp.setData(Qt.DecorationRole, pixmap)
            self.guide_table.setItem(row_position, 0, tmp)

            tmp = QTableWidgetItem(str(guide.name))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 1, tmp)
            self.guide_table.setColumnWidth(1, 150)

            tmp = QTableWidgetItem(str(guide.hero))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 2, tmp)
            self.guide_table.setColumnWidth(2, 100)

            tmp = QTableWidgetItem(str(guide.rating))
            tmp.setTextAlignment(Qt.AlignHCenter)
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 3, tmp)
            self.guide_table.setColumnWidth(3, 40)

            tmp = QTableWidgetItem(str(guide.description))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.guide_table.setItem(row_position, 4, tmp)


        self.table_is_changeable = True

    def search_by(self):
        dictionary = {'name': None,
                      'hero': None,
                      'rating': None,
                      'description': None}

        search_string = self.search_lineEdit.text()
        pairs = search_string.split()
        for pair in pairs:
            key, value = pair.split(":")
            if key in dictionary:
                dictionary[key] = value
        # print(dictionary)
        get_guides = self.session.query(Guide)
        if dictionary['name'] != None:
            get_guides = get_guides.filter(Guide.name == dictionary['name'])
        if dictionary['hero'] != None:
            session = create_session()
            hero = session.query(Hero).filter(Hero.name == dictionary['hero']).first()
            get_guides = get_guides.filter(Guide.hero_id == hero.id)
        if dictionary['rating'] != None:
            get_guides = get_guides.filter(Guide.rating == dictionary['rating'])
        if dictionary['description'] != None:
            get_guides = get_guides.filter(Guide.description == dictionary['description'])
        self.loader(get_guides.all())

    def change_or_view_guide(self, index: QModelIndex):
        current_row = index.row()
        row_name = self.guide_table.item(current_row, 1).text()
        guide_structure = self.session.query(Guide).filter(Guide.name == str(row_name).strip()).first()
        # print(guide_structure)
        self.open_change_or_view_guide = SelectGuideChangeOrView(self.login_structure, self, guide_structure)
        self.open_change_or_view_guide.exec_()
        self.load_all()


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

# TODO: добавить до 100 записей, *хеширование паролей, *страна+-
