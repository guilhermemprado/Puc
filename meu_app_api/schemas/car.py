"""
    Imports
"""
from typing import List

from model import Session
from model.brand import Brand
from model.car import Car
from model.fuel import Fuel
from model.model import Model
from pydantic import BaseModel


class CarSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca."""

    color: str = ""
    year_manufacture: str = ""
    year_model: str = ""
    value: float = 0.00
    model: int = 0
    fuel: int = 0


class CarSearchSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id do carro.
    """

    id: int = 0


def show_cars(cars: List[Car]):
    """Retorna uma representação dos carros seguindo o schema definido em
    CarViewSchema.
    """
    result = []
    for car in cars:
        # criando conexão com a base
        session = Session()
        # Busca o nome do modelo
        query_model = session.query(Model).filter(Model.id == car.model).first()
        query_brand = session.query(Brand).filter(Brand.id == query_model.brand).first()
        query_fuel = session.query(Fuel).filter(Fuel.id == car.fuel).first()
        

        result.append(
            {
                "Id": car.id,
                "Color": car.color,
                "Year_manufacture": car.year_manufacture,
                "Year_model": car.year_model,
                "Value": "{:.2f}".format(car.value),
                "Brand": query_brand.name,
                "Model": query_model.name,
                "Fuel": query_fuel.type,
            }
        )

    return {"cars": result}


def show_car(car: Car):
    """Retorna uma representação da marca seguindo o schema definido em
    BrandViewSchema.
    """
    # criando conexão com a base
    session = Session()
    # Busca o nome do modelo
    query_model = session.query(Model).filter(Model.id == car.model).first()
    query_brand = session.query(Brand).filter(Brand.id == query_model.brand).first()
    query_fuel = session.query(Fuel).filter(Fuel.id == car.fuel).first()

    return {
        "Id": car.id,
        "Color": car.color,
        "Year manufacture": car.year_manufacture,
        "Year model": car.year_model,
        "Value": "{:.2f}".format(car.value),
        "Brand": query_brand.name,
        "Model": query_model.name,
        "Fuel": query_fuel.type,
    }


class UpdateCarSchema(BaseModel):
    """Define como um novo produto pode ser atualizado."""

    color: str = ""
    Year_manufacture: str = ""
    year_model: str = ""
    value: float = 0.00
    model: int = 0
    brand: int = 0
    fuel: int = 0
