import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = relationship("favorites")
    

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    iud = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    height = Column(Integer, nullable=True)
    mass = Column(Integer, nullable=True)
    hair_color = Column(String(45), nullable=True)
    skin_color = Column(String(45), nullable=True)
    eye_color = Column(String(45), nullable=True)
    birth_year = Column(String(45), nullable=True)
    gender = Column(String(45), nullable=True)
    created = Column(DateTime, nullable=True) #confirmar tipo de dato
    edited = Column(DateTime, nullable=True) #confirmar tipo de dato
    description = Column(Text, nullable=True)
    _id = Column(Integer, nullable=True)
    _v = Column(Integer, nullable=True)
    homeworldId = Column(Integer, ForeignKey('planet.uid'))
    people_drive_vehicle = relationship("people_drive_vehicle")
    favorites = relationship("favorites")

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    iud = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    model = Column(String(45), nullable=True)
    vehicle_class = Column(String(45), nullable=True)
    manufacturer = Column(String(45), nullable=True)
    cost_in_credits = Column(Integer, nullable=True)
    length = Column(Float, nullable=True)
    crew = Column(Integer, nullable=True)
    max_atmosphering_speed = Column(Integer, nullable=True)
    cargo_capacity = Column(Integer, nullable=True)
    consumables = Column(String(45), nullable=True)
    created = Column(DateTime, nullable=True) #confirmar tipo de dato
    edited = Column(DateTime, nullable=True) #confirmar tipo de dato
    description = Column(Text, nullable=True)
    _id = Column(Integer, nullable=True)
    _v = Column(Integer, nullable=True)
    people_drive_vehicle = relationship("people_drive_vehicle")
    favorites = relationship("favorites")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    iud = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=True)
    rotation_period = Column(Integer, nullable=True)
    manufacturer = Column(String(45), nullable=True)
    orbital_period = Column(Integer, nullable=True)
    length = Column(Float, nullable=True)
    gravity = Column(Integer, nullable=True)
    population = Column(Integer, nullable=True)
    climate = Column(String(45), nullable=True)
    terrain = Column(String(45), nullable=True)
    surface_water = Column(Integer, nullable=True)
    created = Column(DateTime, nullable=True) 
    edited = Column(DateTime, nullable=True) 
    description = Column(Text, nullable=True)
    _id = Column(Integer, nullable=True)
    _v = Column(Integer, nullable=True)
    favorites = relationship("favorites")

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favorites_id = Column(Integer, primary_key=True)
    People_uid = Column(Integer, ForeignKey('people.uid'))
    Vehicles_uid = Column(Integer, ForeignKey('vehicles.uid'))
    Planets_uid = Column(Integer, ForeignKey('planets.uid'))
    User_uid = Column(Integer, ForeignKey('user.id'))
    people = relationship("people")
    planets = relationship("planets")
    vehicles = relationship("vehicles")
    user = relationship("user")

class People_drive_vehicle(Base):
    __tablename__ = 'people_drive_vehicles'
    people_drive_vehicles_id = Column(Integer, primary_key=True)
    people_uid = Column(Integer, ForeignKey('people.uid'))
    Vehicles_uid = Column(Integer, ForeignKey('vehicles.uid'))
    vehicles = relationship("vehicles")
    user = relationship("user")




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
