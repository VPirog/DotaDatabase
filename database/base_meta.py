import configparser
import sqlalchemy.ext.declarative as dec
import sqlalchemy as sa
import sqlalchemy.orm as orm

Base = dec.declarative_base()

__factory = None

config = configparser.ConfigParser()
config.read('config/config.ini')

database_host = config['database']['host']
database_port = config['database']['port']
database_username = config['database']['username']
database_password = config['database']['password']
database_name = config['database']['name']


def global_init(host=database_host, port=database_port, user=database_username, password=database_password,
                db_name=database_name):
    global __factory

    if __factory:
        return

    if not db_name:
        raise AttributeError("Не задано имя файлы файла базы данных")

    connection_string = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    print(f"Подключение к БД: {connection_string}")

    engine = sa.create_engine(connection_string, echo=True)
    __factory = orm.sessionmaker(engine)


def create_session():
    return __factory()
