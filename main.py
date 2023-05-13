import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication
import resource
from database import global_init, create_session, Hero, Item, User, Guide
from parse.parse import *
import configparser
from ui import LoginScreen
from ui import Registration
from ui import *

global_init()
session = create_session()

# items = session.query(Item).all()
# for i in items:
#     print(i)


# users = session.query(Guide).all()
# for i in users:
#     print(i)
#
# users = session.query(Hero).all()
# for i in users:
#     print(i)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = LoginScreen()
#     ex.show()
#     sys.exit(app.exec())

# async def main():
#     await parsing_image("https://dota2.fandom.com/wiki/Category:Item_icons")
#
# asyncio.run(main())
