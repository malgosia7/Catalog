import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


# set up of table with categories:
class CategoryDBClass(Base):
    __tablename__ = 'category_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

# below is for JSON endpoint:
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


# set up of table with items:
class ItemDBClass(Base):
    __tablename__ = 'item_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(25000))
    category_id = Column(Integer, ForeignKey('category_table.id'))
    category_name = relationship('CategoryDBClass')
    item_pin = Column(String(5))

# below is for JSON endpoint:
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
        }


# below command creates a new file with database named 'catalog.db':
engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
