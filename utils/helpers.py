import requests
from fastapi import HTTPException


# Funciones auxiliares

def get_random_chuck_norris_joke() -> str:
    joke_api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(joke_api_url)
    response.raise_for_status()
    response_key = response.json()

    if "value" in response_key:
        return {"joke": response_key["value"]}
    else:
        raise HTTPException(status_code=500, detail="Error en la API")


def get_random_dad_joke() -> str:
    joke_api_url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(joke_api_url, headers=headers)
    response.raise_for_status()
    response_dic = response.json()

    if "joke" in response_dic:
        return {"joke": response_dic["joke"]}
    else:
        raise HTTPException(status_code=500, detail="Error en la API")

