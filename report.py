from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime


class Report(Base):
    """ Request info """

    __tablename__ = "report"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    customer = Column(String(250), nullable=False)
    pickup = Column(String(250), nullable=False)
    dropoff = Column(String(250), nullable=False)
    pickuptime = Column(String(250), nullable=False)
    dropofftime = Column(String(250), nullable=False)
    rating = Column(String(250), nullable=False)
    notes = Column(String(100), nullable=False)
    date_created = Column(DateTime, nullable=False)

    def __init__(self, name, customer, pickup, dropoff, pickuptime, dropofftime, rating, notes):
        """ Initialize a report  """
        self.name = name
        self.customer = customer
        self.pickup = pickup
        self.dropoff = dropoff
        self.pickuptime = pickuptime
        self.dropofftime = dropofftime
        self.rating = rating
        self.notes = notes
        self.date_created = datetime.datetime.now()

    def to_dict(self):
        """ Dictionary representation of a report """
        dict = {}
        dict['id'] = self.id
        dict['name'] = self.name
        dict['customer'] = self.customer
        dict['pickup'] = self.pickup
        dict['dropoff'] = self.dropoff
        dict['pickuptime'] = self.pickuptime
        dict['dropofftime'] = self.dropofftime
        dict['rating'] = self.rating
        dict['notes'] = self.notes

        return dict