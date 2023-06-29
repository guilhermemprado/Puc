"""
    Imports
"""
from typing import List, Optional

from model import Session
from model.brand import Brand
from model.model import Model
from pydantic import BaseModel


class ModelNameSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id.
    """

    name: str = ""


class ModelSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no id.
    """

    name: str = ""
    brand: int = 0


def show_models(models: List[Model]):
    """Retorna uma representação dos modelos seguindo o schema definido em
    ModelSchema.
    """
    result = []
    for model in models:
        # criando conexão com a base
        session = Session()
        # Busca o nome da marca
        query = session.query(Brand).filter(Brand.id == model.brand).first()

        result.append(
            {
                "Id": model.id,
                "Name": model.name,
                "Brand": query.name,
            }
        )

    return {"Models": result}


def show_model(model: Model):
    """Retorna uma representação do modelo seguindo o schema definido em
    ModelSchema.
    """
    return {
        "Id": model.id,
        "Name": model.name,
        "Brand": model.brand,
    }
