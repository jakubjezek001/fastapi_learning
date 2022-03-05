from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from . import config


# The declarative base we'll use to create our model
Base = declarative_base()
