import sys
from PyQt5.QtWidgets import QApplication
import resource
from database import global_init, create_session, Hero, Item
from parse.parse import parsing
import configparser
import ui
from ui import LoginScreen

config = configparser.ConfigParser()
config.read('config/config.ini')

database_host = config['database']['host']
database_port = config['database']['port']
database_username = config['database']['username']
database_password = config['database']['password']
database_name = config['database']['name']

# global_init(database_host, database_port, database_username, database_password, database_name)
# session = create_session()
#
# items = session.query(Item).all()
#
# for parent in items:
#     print(parent)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginScreen()
    ex.show()
    sys.exit(app.exec())

# parsing("https://liquipedia.net/dota2/Item_statistics")
