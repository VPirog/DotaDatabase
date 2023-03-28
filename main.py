from database import global_init, create_session, Hero

global_init("dota")
session = create_session()

heroes = session.query(Hero).all()

for parent in heroes:
    print(parent)
