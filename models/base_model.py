#!/usr/bin/python3
""" Parent class that defines all attributes/methods
for all other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represents all common attributes from BaseModel"""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Returns string representation of class name, id and
        attribute dictionary
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns dictionary representation of BaseModel instances """

        dict_ = dict(self.__dict__)
        dict_.update({"__class__": self.__class__.__name__,
                      "created_at": str(((self.created_at).isoformat())),
                      "updated_at": str(((self.updated_at).isoformat()))})
        return dict_
