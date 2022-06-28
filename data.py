import json
from main import Connect
from pprint import pprint
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


def read_json(data):
    with open(data, encoding='UTF-8') as file:
        work = json.load(file)
        return work


engine = Connect()
engine.get_dsn()
engine.get_connection()
