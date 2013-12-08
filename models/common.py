# this is a common file for all models
from sqlalchemy import Column, Integer, Boolean, String, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship, backref

