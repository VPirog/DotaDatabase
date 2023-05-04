from database import global_init, create_session, Hero, Item
from parse.parse import parsing

global_init("postgres", "utezam", "localhost", "dota")
session = create_session()

heroes = session.query(Item).all()

for parent in heroes:
    print(parent)

parsing("https://liquipedia.net/dota2/Hero_statistics")
