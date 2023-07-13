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

info = Info(title="Car list", version="1.0.0")
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
@app.post("/car", tags=[car_tag])
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
    "/update_car",
    tags=[car_tag],
)
def update_car(query: CarSearchSchema, form: UpdateCarSchema):
    """Change a car already saved in the database

    Returns a representation of the car.
    """
    try:
        session = Session()
        query = session.query(Car).filter(Car.id == query.id)
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

            if form.year_manufacture:
                db_car.year_manufacture = form.year_manufacture
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

            if form.brand:
                db_car.brand = form.brand
            else:
                error_msg = "Informe a marca."
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


@app.get("/cars", tags=[car_tag])
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


@app.get("/car", tags=[car_tag])
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


@app.delete("/car", tags=[car_tag])
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
@app.get("/brands", tags=[brand_tag])
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


# Modelo
@app.get("/models", tags=[model_tag])
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


# Combustível
@app.get("/fuels", tags=[fuel_tag])
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
