#!/usr/bin/python3
"""
Base Class of all model classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ To be inherited by other model classes """
    def __init__(self, *args, **kwargs):
        """ Attribute initializer """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(kwargs[k], "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    setattr(self, k, v)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        storage.new(self)

    def __str__(self):
        """ Returns the string representation of the class """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """ Sets updated_at attribute to the current date and time """
        self.updated_at = datetime.now()

