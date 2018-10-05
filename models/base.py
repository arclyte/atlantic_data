from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database():
    def __init__(self):
        Session = sessionmaker(bind=self.db_connect())
        self.session = Session()

    def db_connect(self):
        return create_engine('mysql+pymysql://root:@localhost/atlantic_data?charset=utf8mb4')


db = Database()
