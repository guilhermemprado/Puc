from model import Base
from sqlalchemy import Column, Integer, String


class Model(Base):
    __tablename__ = "model"

    id = Column("id", Integer, primary_key=True)
    name = Column(String, unique=True)
    brand = Column("brand", Integer)

    def __init__(
        self,
        name: str,
        brand: int,
    ):
        """
        Cria uma model

        Arguments:
            name: Create model
        """
        self.name = name
        self.brand = brand
