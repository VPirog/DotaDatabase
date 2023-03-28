from database import create_session, global_init, Hero

global_init("dota")
session = create_session()

heroes = session.query(Hero).all()

for parent in heroes:
    print(parent)
