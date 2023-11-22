from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """
    This is the class for User.

    Attributes:
        email (str): email address
        password (str): password for login
        first_name (str): first name
        last_name (str): last name
        places (relationship): relationship with Place model
        reviews (relationship): relationship with Review model
    """
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship(
        "Place",
        cascade='all, delete, delete-orphan',
        backref="user"
    )

    reviews = relationship(
        "Review",
        cascade='all, delete, delete-orphan',
        backref="user"
    )
