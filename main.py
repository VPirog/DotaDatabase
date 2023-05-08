from database import global_init, create_session, Hero, Item
from parse.parse import parsing
import configparser

config = configparser.ConfigParser()
config.read('config/config.ini')

database_host = config['database']['host']
database_port = config['database']['port']
database_username = config['database']['username']
database_password = config['database']['password']
database_name = config['database']['name']

global_init(database_host, database_port, database_username, database_password, database_name)
session = create_session()

items = session.query(Item).all()

for parent in items:
    print(parent)

# parsing("https://liquipedia.net/dota2/Item_statistics")
