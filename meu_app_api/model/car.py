"""
    Imports
"""
from model import Base
from sqlalchemy import Column, Integer, String, Float


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True)
    color = Column(String(50))
    year_manufacture = Column(String(4))
    year_model = Column(String(4))
    value = Column(Float)
    model = Column(Integer)
    fuel = Column(Integer)

    def __init__(
        self,
        color: str,
        year_manufacture: str,
        year_model: str,
        value: float,
        model: int,
        fuel: int,
    ):
        """
        Cria model carro
        """
        self.color = color
        self.year_manufacture = year_manufacture
        self.year_model = year_model
        self.value = value
        self.model = model
        self.fuel = fuel
