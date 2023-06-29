from model import Base
from sqlalchemy import Column, Integer, String


class Brand(Base):
    __tablename__ = "brand"

    id = Column("id", Integer, primary_key=True)
    name = Column(String, unique=True)

    def __init__(
        self,
        name: str,
    ):
        """
        Cria uma brand

        Arguments:
            name: Car brand name
        """
        self.name = name
