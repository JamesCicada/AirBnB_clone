#!/usr/bin/python3
"""Defines State class."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state.

    Attributes:
        name (str):  name of the state.
    """

    name = ""
