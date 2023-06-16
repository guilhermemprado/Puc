from pydantic import BaseModel


class ProdutoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """


class ProdutoBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do produto.
    """
