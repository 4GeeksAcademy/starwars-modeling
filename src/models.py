import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String, nullable=True)
    def serialize(self):
        return {
            'email': self.email,
            'username': self.username
            }

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    population = Column(Integer, nullable=False)
    def serialize(self):
        return {
            'name': self.name,
            'population': self.population
            }
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age
            }

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    top_speed = Column(Integer, nullable=False)
    def serialize(self):
        return {
            'name': self.name,
            'top_speed': self.top_speed
            }

class FavoriteList(Base):
    __tablename__ = 'favoriteList'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    planet = relationship(Planet)
    character = relationship(Character)
    vehicle = relationship(Vehicle)
    def serialize(self):
        return {
            'planet': self.planet,
            'user': self.user,
            'vehicle': self.vehicle,
            'character': self.character
            }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
