#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel class for the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        # Date format for string to datetime conversion
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        # Assign a unique identifier to the instance
        self.id = str(uuid4())

        # Set the creation and update timestamps to the current datetime
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        # If keyword arguments are provided, update instance attributes
        if kwargs:
            for key, value in kwargs.items():
                # Convert string to datetime for specific attributes
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            # If no kwargs, add the instance to the storage system
            models.storage.new(self)

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance.

        Includes the key/value pair '__class__' representing the class name.
        """
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
