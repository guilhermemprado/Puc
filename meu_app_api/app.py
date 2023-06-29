"""
    Imports
"""
from urllib.parse import unquote

from flask import redirect
from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI, Tag
from model import Session, __init__
from model.brand import Brand
from model.car import Car
from model.fuel import Fuel
from model.model import Model
from schemas.brand import BrandSchema, show_brand, show_brands
from schemas.car import CarSchema, CarSearchSchema, UpdateCarSchema, show_car, show_cars
from schemas.fuel import FuelSchema, show_fuel, show_fuels
from schemas.model import ModelNameSchema, ModelSchema, show_model, show_models
from sqlalchemy.exc import IntegrityError

info = Info(title="My API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(
    name="Documentation",
    description="Documentation selection: Swagger, Redoc or RapiDoc.",
)
car_tag = Tag(name="Car", description="Create, Change, view and delete car based.")
brand_tag = Tag(
    name="Brand",
    description="Create, view and delete a car brand database.",
)
model_tag = Tag(
    name="Model",
    description="Create, view and delete a car model from the database.",
)
fuel_tag = Tag(
    name="Fuel",
    description="Create, view and delete fuel type from car database.",
)


# Documentação
@app.get("/", tags=[home_tag])
def home():
    """Redirects to /openapi, screen that allows choosing the documentation style."""
    return redirect("/openapi")


# Produto
@app.post("/carro", tags=[car_tag])
def new_car(form: CarSchema):
    """Add a new car to the database

    Returns a representation of cars.
    """
    car = Car(
        color=form.color.lower().capitalize(),
        year_manufacture=form.year_manufacture,
        year_model=form.year_model,
        value=form.value,
        model=form.model,
        fuel=form.fuel,
    )
    try:
        # criando conexão com a base
        session = Session()
        # adicionando carro
        session.add(car)
        # efetivando o camando de adição de novo item na tabela
        session.commit()

        return show_car(car), 200

    except IntegrityError as error:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = f"Carro já salvo na base: {error}"
        return {"mesage": error_msg}, 409

    except Exception:
        # caso um erro fora do previsto
        error_msg = f"Não foi possível alterar o item: {error}"
        return {"mesage": error_msg}, 400


@app.post(
    "/update_carro",
    tags=[car_tag],
)
def update_car(query: CarSearchSchema, form: UpdateCarSchema):
    """Change a car already saved in the database

    Returns a representation of the car.
    """
    try:
        session = Session()
        query = session.query(Car).filter(Car.id == query.id)
        print(query)
        db_car = query.first()
        if not db_car:
            # Se o carro não foi encontrado
            error_msg = "Carro não encontrado na base."
            return {"mesage": error_msg}, 404
        else:
            if form.color:
                db_car.color = form.color
            else:
                error_msg = "Informe a cor."
                return {"mesage": error_msg}, 404

            if form.Year_manufacture:
                db_car.Year_manufacture = form.Year_manufacture
            else:
                error_msg = "Informe o ano de fabricação."
                return {"mesage": error_msg}, 404

            if form.year_model:
                db_car.year_model = form.year_model
            else:
                error_msg = "Informe o ano do modelo."
                return {"mesage": error_msg}, 404

            if form.model:
                db_car.model = form.model
            else:
                error_msg = "Informe o modelo."
                return {"mesage": error_msg}, 404

            if form.value:
                db_car.value = form.value
            else:
                error_msg = "Informe o valor."
                return {"mesage": error_msg}, 404

            if form.fuel:
                db_car.fuel = form.fuel
            else:
                error_msg = "Informe o combustível."
                return {"mesage": error_msg}, 404

            session.add(db_car)
            session.commit()
            return show_car(db_car), 200

    except Exception:
        # caso um erro fora do previsto
        error_msg = "Não foi possível alterar o item."
        return {"mesage": error_msg}, 400


@app.get("/carros", tags=[car_tag])
def get_cars():
    """Search for all registered cars

    Returns a representation of the car listing.
    """
    session = Session()
    # fazendo a busca
    cars = session.query(Car).all()

    if not cars:
        # se não há carros cadastrados
        return {"carro": []}, 200
    else:
        # retorna a representação de carros
        return show_cars(cars), 200


@app.get("/carro", tags=[car_tag])
def get_car(query: CarSearchSchema):
    """Searches for a car based on the car id

    Returns a representation of cars.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    car = session.query(Car).filter(Car.id == query.id).first()

    if not car:
        # se o produto não foi encontrado
        error_msg = "Carro não encontrado na base :/"
        return {"mesage": error_msg}, 404
    else:
        # retorna a representação de produto
        return show_car(car), 200


@app.delete("/carro", tags=[car_tag])
def delete_car(query: CarSearchSchema):
    """Deletes a car from the informed car id

    Returns a removal confirmation message.
    """
    car_id = unquote(unquote(str(query.id)))

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Car).filter(Car.id == car_id).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Carro removido", "id": car_id}
    else:
        # Se a marca não foi encontrado
        error_msg = f"Carro id: {car_id} não encontrado na base:"
        return {"mesage": error_msg}, 404


# Marca
@app.get("/marca", tags=[brand_tag])
def get_brand():
    """Search for all registered brands

    Returns a representation of the tag listing.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    brands = session.query(Brand).all()

    if not brands:
        # se não há marcas cadastrados
        return {"marcas": []}, 200
    else:
        # retorna a representação da marca
        return show_brands(brands), 200


@app.post("/marca", tags=[brand_tag])
def new_brand(form: BrandSchema):
    """Adds a new tag to the database

    Returns a representation of the added tag.
    """
    brand = Brand(name=form.name.lower().capitalize())
    try:
        # criando conexão com a base
        session = Session()
        # adicionando marca
        session.add(brand)
        # efetivando o camando de adição de novo item na tabela
        session.commit()

        return show_brand(brand), 200

    except IntegrityError:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Produto de mesmo nome já salvo na base:"
        return {"mesage": error_msg}, 409

    except Exception:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item:"
        return {"mesage": error_msg}, 400


@app.delete("/marca", tags=[brand_tag])
def delete_brand(query: BrandSchema):
    """Deletes a tag from the given tag name

    Returns a removal confirmation message.
    """
    brand_name = unquote(unquote(query.name.lower().capitalize()))

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Brand).filter(Brand.name == brand_name).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Marca removida", "id": brand_name}
    else:
        # Se a marca não foi encontrado
        error_msg = f"Marca {brand_name} não encontrado na base:"
        return {"mesage": error_msg}, 404


# Modelo
@app.get("/modelo", tags=[model_tag])
def get_model():
    """Searches for all registered models

    Returns a representation of the model listing.
    """
    session = Session()
    # fazendo a busca
    models = session.query(Model).all()

    if not models:
        # se não há modelo cadastrados
        return {"modelo": []}, 200
    else:
        # retorna a representação de modelo
        return show_models(models), 200


@app.post("/modelo", tags=[model_tag])
def new_model(form: ModelSchema):
    """Adds a new model to the database

    Returns an added representation of the model.
    """
    model = Model(name=form.name.lower().capitalize(), brand=form.brand)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando modelo
        session.add(model)
        # efetivando o camando de adição de novo item na tabela
        session.commit()

        return show_model(model), 200

    except IntegrityError:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Modelo de mesmo nome já salvo na base:"
        return {"mesage": error_msg}, 409

    except Exception:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item:"
        return {"mesage": error_msg}, 400


@app.delete("/modelo", tags=[model_tag])
def delete_model(query: ModelNameSchema):
    """Deletes a model from the given id.

    Returns a removal confirmation message.
    """
    model_name = unquote(unquote(query.name.lower().capitalize()))

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Model).filter(Model.name == model_name).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Modelo removido", "nome": model_name}
    else:
        # Se a marca não foi encontrado
        error_msg = f"Modelo {model_name} não encontrado na base:"
        return {"mesage": error_msg}, 404


# Combustível
@app.get("/combustivel", tags=[fuel_tag])
def get_fuel():
    """Searches for all registered fuel types.

    Returns a representation of the fuel listing.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    fuels = session.query(Fuel).all()

    if not fuels:
        # se não há combustível cadastrados
        return {"marcas": []}, 200
    else:
        # retorna a representação de combustível
        return show_fuels(fuels), 200


@app.post("/combustivel", tags=[fuel_tag])
def new_fuel(form: FuelSchema):
    """Adds a new fuel to the database.

    Returns a representation of the added fuel.
    """
    fuel = Fuel(type=form.type.lower().capitalize())
    try:
        # criando conexão com a base
        session = Session()
        # adicionando combustível
        session.add(fuel)
        # efetivando o camando de adição de novo item na tabela
        session.commit()

        return show_fuel(fuel), 200

    except IntegrityError:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Combustível de mesmo nome já salvo na base:"
        return {"mesage": error_msg}, 409

    except Exception:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item:"
        return {"mesage": error_msg}, 400


@app.delete("/combustivel", tags=[fuel_tag])
def delete_fuel(query: FuelSchema):
    """Deletes a fuel from the given id.

    Returns a removal confirmation message.
    """
    fuel_type = unquote(unquote(query.type.lower().capitalize()))

    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Fuel).filter(Fuel.type == fuel_type).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        return {"mesage": "Combustível removido", "tipo": fuel_type}
    else:
        # Se a marca não foi encontrado
        error_msg = f"Combustível {fuel_type} não encontrado na base:"
        return {"mesage": error_msg}, 404
