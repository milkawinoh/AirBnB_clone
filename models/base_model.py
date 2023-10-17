#!/usr/bin/python3


import uuid
from datetime import datetime
"""
This module serves as the base model
for all objects in the AirBnB project.
It contains common attributes and methods shared by all other classes.
"""


class BaseModel:
    """
    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The timestamp for
            when the instance was created.
        updated_at (datetime): The timestamp
        for when the instance was last updated.

    Methods:
        __init__(self): Initializes a new instance
        of the BaseModel class.
        __str__(self): Returns a string representation
        of the BaseModel instance.
        save(self): Updates the attribute 'updated_at'
        with the current datetime.
        to_dict(self): Returns a dictionary containing
        all key/value pairs of the instance.
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            updated_kwargs = {}
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    updated_kwargs[key] = value
                    self.__dict__.update(updated_kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            from models import storage
            storage.new(self)

    def __str__(self):
        """Return a string representation."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                              self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """Return a dictionary containing
        all keys/values of __dict__ of the instance."""
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
