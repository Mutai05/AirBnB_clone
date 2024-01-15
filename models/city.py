#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city.

    Attributes:
        state_id (str): The identifier of the state associated with the city.
        name (str): The name of the city.
    """

    # Default empty strings for state_id and city name
    state_id = ""
    name = ""
