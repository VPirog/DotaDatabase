import hashlib
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


# password = "my_password"
# saved_hashed_password = "f6e248ea994f3e342f61141b8b8e3ede86d4de53257abc8d06ae07a1da73fb39"
#
# # Создание объекта хеша
# hash_object = hashlib.sha256()
#
# # Кодирование пароля в байтовую строку и хеширование
# hash_object.update(password.encode("utf-8"))
# hashed_password = hash_object.hexdigest()
# print(hashed_password)
#
# # Сравнение хешей
# if hashed_password == saved_hashed_password:
#     print("Пароль верен")
# else:
#     print("Пароль неверен")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoginScreen()
    ex.show()
    sys.exit(app.exec())

# async def main():
#     await parsing_image("https://dota2.fandom.com/wiki/Category:Item_icons")
#
# asyncio.run(main())
