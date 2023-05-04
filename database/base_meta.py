import sqlalchemy.ext.declarative as dec
import sqlalchemy as sa
import sqlalchemy.orm as orm

Base = dec.declarative_base()

__factory = None


def global_init(user, password, host, db_name):
    global __factory

    if __factory:
        return

    if not db_name:
        raise AttributeError("Не задано имя файлы файла базы данных")

    connection_string = f'postgresql://{user}:{password}@{host}:5432/{db_name}'
    print(f"Подключение к БД: {connection_string}")

    engine = sa.create_engine(connection_string, echo=True)
    __factory = orm.sessionmaker(engine)


def create_session():
    return __factory()
