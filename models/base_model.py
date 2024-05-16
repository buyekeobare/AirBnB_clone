#!/usr/bin/python3
"""
This script defines the BaseModel class.
The uuid module is used for the creation of unique id.
Date and time module help us work with time.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    """The super class from which all other classes will inherit from."""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel

        Args:
            - *args: arguments list (not used)
            - **kwargs: dictionary of key-values/keyword arguments.
        """

        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the str representation of an instance"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the instance attribute updated_at with current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict containing all keys/values of __dict__"""

        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
