"""
    Imports
"""
from typing import List, Optional

from model.brand import Brand
from pydantic import BaseModel


class BrandSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id.
    """

    name: str = ""


def show_brands(brands: List[Brand]):
    """Retorna uma representação das marcas seguindo o schema definido em
    BrandViewSchema.
    """
    result = []
    for brand in brands:
        result.append(
            {
                "Id": brand.id,
                "Name": brand.name,
            }
        )

    return {"Brands": result}


def show_brand(brand: Brand):
    """Retorna uma representação da marca seguindo o schema definido em
    BrandViewSchema.
    """
    return {
        "Id": brand.id,
        "Name": brand.name,
    }
