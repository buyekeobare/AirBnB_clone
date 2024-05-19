"""This script initializes the package"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

from .base_model import BaseModel
from .user import User
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State
