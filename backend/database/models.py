"""
Database Models
"""

from sqlalchemy import Column, Integer, String

from backend.database.database import Base


class Route(Base):

    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String(100))
    destination = Column(String(100))


class Bus(Base):

    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)
    bus_number = Column(String(20))
    bus_name = Column(String(100))
    route = Column(String(100))
    departure_time = Column(String(20))
    fare = Column(Integer)


class Passenger(Base):

    __tablename__ = "passengers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    mobile = Column(String(15))
    age = Column(Integer)
    gender = Column(String(10))


class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String(30))
    passenger_name = Column(String(100))
    bus_number = Column(String(20))
    route = Column(String(100))
    seat_number = Column(String(10))
    journey_date = Column(String(20))
    departure_time = Column(String(20))
    fare = Column(Integer)
    status = Column(String(20))
