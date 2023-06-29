from model import Base
from sqlalchemy import Column, Integer, String


class Fuel(Base):
    __tablename__ = "fuel"

    id = Column("id", Integer, primary_key=True)
    type = Column(String, unique=True)

    def __init__(
        self,
        type: str,
    ):
        """
        Cria uma fuel

        Arguments:
            name: Create a type of fuel
        """
        self.type = type
