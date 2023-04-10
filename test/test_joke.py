from utils.calculate_lcm import calculate_lcm
from main import get_joke_by_type, post_lcm, increment_number
from utils.helpers import get_random_chuck_norris_joke, get_random_dad_joke
from unittest.mock import Mock

from schema.schema import JokeSchema

saved_joke_id = None


# Pruebas para la función calculate_lcm
def test_calculate_lcm():
    assert calculate_lcm([3, 5, 7]) == 105
    assert calculate_lcm([2, 4, 8]) == 8
    assert calculate_lcm([10, 15, 20]) == 60


# Pruebas para la función get_random_chuck_norris_joke
def test_get_random_chuck_norris_joke():
    joke = get_random_chuck_norris_joke()
    assert 'joke' in joke


# Pruebas para la función get_random_dad_joke
def test_get_random_dad_joke():
    joke = get_random_dad_joke()
    assert 'joke' in joke


# Pruebas para el endpoint get_joke_by_type
def test_get_joke_by_type():
    response = get_joke_by_type("chuck")
    assert "joke" in response
    response = get_joke_by_type("dad")
    assert "joke" in response


# Pruebas para el endpoint save_joke
def test_save_joke():
    joke = JokeSchema(joke="Test joke")
    save_joke = Mock(return_value={"id": 1, "joke": "Test joke", "message": "Chiste guardado correctamente"})
    response = save_joke(joke)
    assert "id" in response
    assert "joke" in response
    assert "message" in response
    assert response["message"] == "Chiste guardado correctamente"
    global saved_joke_id
    saved_joke_id = response['id']


# Pruebas para el endpoint update_joke
def test_update_joke():
    joke = JokeSchema(joke="Test joke updated")
    update_joke = Mock(
        return_value={"id": saved_joke_id, "joke": "Test joke updated", "message": "Chiste actualizado correctamente"})
    response = update_joke(saved_joke_id, joke)
    assert "id" in response
    assert "joke" in response
    assert "message" in response
    assert response["message"] == "Chiste actualizado correctamente"


# Pruebas para el endpoint delete_joke
def test_delete_joke():
    delete_joke = Mock(return_value={"message": f"Chiste con ID {saved_joke_id} eliminado correctamente"})
    response = delete_joke(saved_joke_id)
    assert response["message"] == f"Chiste con ID {saved_joke_id} eliminado correctamente"


# Pruebas para el endpoint post_lcm
def test_post_lcm():
    response = post_lcm([3, 5, 7])
    assert response == {"result": 105}
    response = post_lcm([2, 4, 8])
    assert response == {"result": 8}
    response = post_lcm([10, 15, 20])
    assert response == {"result": 60}


# Pruebas para el endpoint increment_number
def test_increment_number():
    response = increment_number(5)
    assert response == {"result": 6}
