from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.model import Pets
DATABASE = 'mysql'
USER = 'root'
PASSWORD = ''
HOST = 'localhost'
PORT = '5431'
DB_NAME = 'animal_db'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(
    DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

ENGINE = None
SESSION = None


def read_data(name):
    local_session = SESSION()
    try:
        pets = local_session.query(Pets).filter(Pets.name == "pochi").all()

        for pet in pets:
            print(pet)

    finally:
        local_session.close()


if __name__ == "__main__":
    ENGINE = create_engine(CONNECT_STR)
    SESSION = sessionmaker(ENGINE)
    print('--------------- before select 1 ------------------------')
    print('  session:{}'.format(ENGINE.pool.status()))

    read_data('pochi')
    print('--------------- after select 1 ------------------------')
    print('  session:{}'.format(ENGINE.pool.status()))

    print('--------------- before select 2 ------------------------')
    print('  session:{}'.format(ENGINE.pool.status()))
    read_data('tama')
