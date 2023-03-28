from database import global_init, create_session, Hero
from parse.parse import parsing

global_init("dota")
session = create_session()

heroes = session.query(Hero).all()

for parent in heroes:
    print(parent)

parsing("https://liquipedia.net/dota2/Item_statistics")