from typing import List, Optional
from datetime import datetime
from random import choice

from fastapi import FastAPI, HTTPException, Query, status

from config.database import Session
from config.model import Joke
from schema.schema import JokeSchema

from utils.calculate_lcm import validate_numbers, calculate_lcm
from utils.helpers import get_random_chuck_norris_joke, get_random_dad_joke

app = FastAPI()
db = Session()

app.title = "JOKE FastAPI"
app.version = "0.0.1"


# Endpoints Query API's

@app.get("/jokes")
def get_joke_by_type(joke_type: Optional[str] = Query(None)) -> dict:
    if joke_type is None:
        return choice([get_random_chuck_norris_joke(), get_random_dad_joke()])
    elif joke_type.lower() == "chuck":
        return get_random_chuck_norris_joke()
    elif joke_type.lower() == "dad":
        return get_random_dad_joke()
    else:
        return {"error": "Valor de tipo de chiste inválido"}


# Endpoints Created updated Delete

@app.post("/save_joke")
def save_joke(joke: JokeSchema) -> dict:
    # Crea una instancia de la clase Joke con los datos recibidos
    new_joke = Joke(
        joke=joke.joke,
        created_at=datetime.now()
    )
    # Guarda el chiste en la base de datos
    db.add(new_joke)
    db.commit()

    return {
        "id": new_joke.id,
        "joke": new_joke.joke,
        "message": "Chiste guardado correctamente"
    }


@app.put("/update_joke/{joke_id}")
def update_joke(joke_id: int, joke: JokeSchema) -> dict:
    # Busca el chiste en la base de datos
    joke_db = db.query(Joke).filter_by(id=joke_id).first()
    if not joke_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chiste no encontrado")

    # Actualiza los datos del chiste
    joke_db.updated_at = datetime.now()
    joke_data = joke.dict(exclude_unset=True)
    for key, value in joke_data.items():
        setattr(joke_db, key, value)

    # Guarda los cambios en la base de datos
    db.add(joke_db)
    db.commit()

    return {
        "id": joke_id,
        "joke": joke_db.joke,
        "message": "Chiste actualizado correctamente"
    }


@app.delete("/delete_joke/{joke_id}")
def delete_joke(joke_id: int) -> dict:
    # Busca el chiste en la base de datos
    joke = db.query(Joke).get(joke_id)

    # Si no se encuentra el chiste con ese ID, devuelve un error 404
    if not joke:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El chiste no se encuentra")

    # Borra el chiste de la base de datos
    db.delete(joke)
    db.commit()

    return {"message": f"Chiste con ID {joke_id} eliminado correctamente"}


# Endpoints mathematical

@app.post("/lcm")
def post_lcm(
    numbers: List[int] = Query(
        ...,
        ge=1,
        description="calculate the least common multiple"
    )
) -> dict:
    """Calculates the least common multiple of a list of integers."""
    numbers = numbers

    is_valid, error_message = validate_numbers(numbers)
    if not is_valid:
        return {"error": error_message}

    lcm = calculate_lcm(numbers)

    return {"result": lcm}


@app.get("/increment")
def increment_number(
        number: int = Query(
            ...,
            ge=0,
            description="Increments the provided number by 1"
        )
) -> dict:
    return {"result": number + 1}
