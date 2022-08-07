from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Pets(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    birthday = Column(DateTime)

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __str__(self):
        return 'id:{}, name:{}, age:{}, birthday:{}'.format(self.id, self.name, self.age, self.birthday)
