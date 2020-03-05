from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime


class Request(Base):
    """ Request info """

    __tablename__ = "request"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    destination = Column(String(250), nullable=False)
    time = Column(String(250), nullable=False)
    notes = Column(String(250), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, name, location, destination, time, notes):
        """ Initialize a request submission """
        self.name = name
        self.location = location
        self.destination = destination
        self.time = time
        self.notes = notes
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        """ Dictionary representation of a request submission """
        dict = {}
        dict['id'] = self.id
        dict['name'] = self.name
        dict['location'] = self.location
        dict['destination'] = self.destination
        dict['time'] = self.time
        dict['notes'] = self.notes

        return dict