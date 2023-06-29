from typing import List, Optional

from model.fuel import Fuel
from pydantic import BaseModel


class FuelSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id.
    """

    type: str = ""


def show_fuels(fuels: List[Fuel]):
    """Retorna uma representação das marcas seguindo o schema definido em
    FuelSchema.
    """
    result = []
    for fuel in fuels:
        result.append(
            {
                "Id": fuel.id,
                "Type": fuel.type,
            }
        )

    return {"Fuels": result}


def show_fuel(fuel: Fuel):
    """Retorna uma representação da marca seguindo o schema definido em
    FuelSchema.
    """
    return {
        "Id": fuel.id,
        "Type": fuel.type,
    }
