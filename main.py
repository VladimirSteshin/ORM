


def get_dsn():
    config = configparser.ConfigParser()
    config.read('config.ini')
    system = config["Postgres"]["system"]
    name = config["Postgres"]["name"]
    password = config["Postgres"]["password"]
    db_name = config["Postgres"]["db_name"]
    DSN = f"{system}://{name}:{password}@localhost:5432/{db_name}"
    return DSN


def get_engine(dsn):
    engine = sq.create_engine(dsn)


def get_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()


def read_json(data):
    with open(data, encoding='UTF-8') as file:
        work = json.load(file)
        return work
