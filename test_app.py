import requests_mock
from app import get_pokemon


def test_get_pokemon():
    with requests_mock.Mocker() as m:
        m.get("https://pokeapi.co/api/v2/pokemon/pikachu", json={"name": "pikachu"})
        result = get_pokemon("pikachu")
        assert result == {"name": "pikachu"}


def test_get_pokemon_not_found():
    with requests_mock.Mocker() as m:
        m.get("https://pokeapi.co/api/v2/pokemon/charmander", status_code=404)
        result = get_pokemon("charmander")
        assert "HTTP Error: 404 Client Error" in result
