#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import shlex
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        db = models.storage.all()
        lst = []
        rslt = []

        for key in db:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lst.append(db[key])
        for i in lst:
            if (i.state_id == self.id):
                rslt.append(i)
        return rslt
