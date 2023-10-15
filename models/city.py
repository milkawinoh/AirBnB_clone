#!/usr/bin/python3
from models.base_model import BaseModel
"""This module defines the City object."""


class City(BaseModel):
    """This class defines the City object.

    Attributes:
        state_id (str): The ID of the state that the city is in.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
