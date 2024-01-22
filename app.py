import requests
from typing import Union, Dict, Any
from fastapi import FastAPI


def get_pokemon(name: str) -> Union[Dict[str, Any], str]:
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        return f"HTTP Error: {errh}"
    except requests.exceptions.ConnectionError as errc:
        return f"Error Connecting: {errc}"
    except requests.exceptions.Timeout as errt:
        return f"Timeout Error: {errt}"
    except requests.exceptions.RequestException as err:
        return f"Something went wrong: {err}"


app = FastAPI()


@app.get("/")
def read_root():
    data = get_pokemon("pikachu")
    return data
