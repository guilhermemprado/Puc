"""Imports
"""
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect

from schemas.produto import ProdutoSchema, ProdutoBuscaSchema


info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/produto', tags=[produto_tag])
def add_produto():
    """Adiciona um novo Produto à base de dados
    Retorna uma representação dos produtos e comentários associados.
    """
    return "Method post /produto"


@app.put('/produto', tags=[produto_tag])
def alter_produto():
    """Altera um Produto a partir do id informado
    Retorna uma mensagem de confirmação da alteração.
    """
    return "Method put /produto"


@app.get('/produtos', tags=[produto_tag])
def get_produtos():
    """Faz a busca por todos os Produto cadastrados
    Retorna uma representação da listagem de produtos.
    """
    return "Method get /produtos"


@app.get('/produto', tags=[produto_tag])
def get_produto():
    """Faz a busca por um Produto a partir do id do produto
    Retorna uma representação dos produtos e comentários associados.
    """
    return "Method get /produto"


@app.delete('/produto', tags=[produto_tag])
def del_produto():
    """Deleta um Produto a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    return "Method delete /produto"
