#!/usr/bin/python3
"""Defines the Place class."""
from models.base_model import BaseModel

class Place(BaseModel):
    """Represents a place.

    Attributes:
        city_id (str): The identifier of the associated city.
        user_id (str): The identifier of the associated user.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed.
        price_by_night (int): The nightly price of the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): A list of Amenity identifiers associated with the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
