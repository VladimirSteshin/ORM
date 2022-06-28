import json
import configparser
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from data import create_tables, Publisher, Book, Shop, Stock, Sale


def get_dsn():
    config = configparser.ConfigParser()
    config.read('config.ini')
    system = config["Postgres"]["system"]
    name = config["Postgres"]["name"]
    password = config["Postgres"]["password"]
    db_name = config["Postgres"]["db_name"]
    host = config["Postgres"]["host"]
    port = config["Postgres"]["port"]
    DSN = f"{system}://{name}:{password}@{host}:{port}/{db_name}"
    return DSN


def get_engine():
    dsn = get_dsn()
    engine = sq.create_engine(dsn)
    return engine


def fill_db():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    with open('test_data.json', encoding='UTF-8') as file:
        work = json.load(file)
        for data in work:
            model = {
                'publisher': Publisher,
                'book': Book,
                'shop': Shop,
                'stock': Stock,
                'sale': Sale
            }[data.get('model')]
            session.add(model(id=data.get('pk'), **data.get('fields')))
        session.commit()
    session.close()


def find_publisher(publisher):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    if str(publisher).isdigit():
        q = session.query(Book).join(Stock.book).filter(Book.id_publisher == publisher)
        for book in q.all():
            print(book.id_publisher)


create_tables(get_engine())
fill_db()
find_publisher(1)
