from sqlalchemy import Column, Integer, Text, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from settings import DBCONNECTION

Base = declarative_base()


class Fighters(Base):
    __tablename__ = 'fighters'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(Text)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)


class Events(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(Text)
    date = Column(Date)
    addresses = relationship("Fighters", backref="fighters")

engine = create_engine(DBCONNECTION)
session = sessionmaker(bind=engine)()

Base.metadata.create_all(engine)
