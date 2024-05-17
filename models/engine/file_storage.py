#!/usr/bin/python3
"""Defines FileStorage class."""

from models.user import User
from models.state import State
from models.city import City
import json
from models.base_model import BaseModel
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents abstracted storage engine.

    Attributes:
        __file_path (str):  name of the file to save objects to.
        __objects (dict): A dictionary of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serializes __objects to  JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for k in objdict.values():
                    cls_name = k["__class__"]
                    del k["__class__"]
                    self.new(eval(cls_name)(**k))
        except FileNotFoundError:
            return
