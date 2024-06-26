#!/usr/bin/python3
"""Defines Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review.

    Attributes:
        place_id (str):  Id of the place.
        user_id (str):  User id.
        text (str): the text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
