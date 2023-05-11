import sys
from PyQt5.QtWidgets import QApplication
import resource
from database import global_init, create_session, Hero, Item, User
from parse.parse import parsing
import configparser
from ui import LoginScreen
from ui import Registration
from ui import GuideView

global_init()
session = create_session()

# items = session.query(Item).all()
# for i in items:
#     print(i)


users = session.query(User).all()
for i in users:
    print(i)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginScreen()
    ex.show()
    sys.exit(app.exec())

# parsing("https://liquipedia.net/dota2/Hero_statistics")
