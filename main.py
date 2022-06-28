import os
import configparser
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


class Connect:
    def __init__(self):
        self.session = None
        self.engine = None
        self.DSN = None
        self.config = 'config.ini'

    def get_dsn(self):
        config = configparser.ConfigParser()
        config.read(self.config)
        system = config["Postgres"]["system"]
        name = config["Postgres"]["name"]
        password = config["Postgres"]["password"]
        db_name = config["Postgres"]["db_name"]
        self.DSN = f"{system}://{name}:{password}@localhost:5432/{db_name}"

    def get_connection(self):
        self.engine = sq.create_engine(self.DSN)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def end(self):
        self.session.close()
