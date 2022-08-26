import pytest
import json

import sys
sys.path.insert(1, "../")

from controllers import app  # noqa: E402


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_invalid_encode_route(client):
    """
    Testing the encode route without passing the parameter.
    It must return a 404_NOT_FOUND status
    """
    result = client.get("/encode")

    assert result.status_code == 404


def test_invalid_decode_route(client):
    """
    Testing the decode route without passing the parameter.
    It must return a 404_NOT_FOUND status
    """
    result = client.get("/decode")

    assert result.status_code == 404


def test_encode_with_invalid_parameter(client):
    """Testing the encode route with an invalid input (not a number)"""

    result = client.get("/encode/2-9asw38")

    assert result.status_code == 404


def test_decode_with_wrong_format_parameter(client):
    """
    Testing the decode route with a valid length code, but on a wrong format
    """

    result = client.get("/decode/2039ei")

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": "Invalid code"}


def test_decode_with_lower_length_parameter(client):
    """
    Testing the decode route with a valid format code, but on a lower length
    """

    result = client.get("/decode/2VBO7")

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": "Invalid code"}


def test_decode_with_bigger_length_parameter(client):
    """
    Testing the decode route with a valid format code, but on a bigger length
    """

    result = client.get("/decode/2VBO7V3")

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {"message": "Invalid code"}


def test_encode_with_one_number(client):
    """Testing the encode route with one number"""

    result = client.get("/encode/1")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "1====="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_two_numbers(client):
    """Testing the encode route with two numbers"""

    result = client.get("/encode/22")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "M====="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_three_numbers(client):
    """Testing the encode route with three numbers"""

    result = client.get("/encode/435")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "DJ===="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_four_numbers(client):
    """Testing the encode route with four numbers"""

    result = client.get("/encode/2522")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "2EQ==="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_five_numbers(client):
    """Testing the encode route with five numbers"""

    result = client.get("/encode/98536")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "3078=="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_six_numbers(client):
    """Testing the encode route with six numbers"""

    result = client.get("/encode/548697")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "GNQP=="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_seven_numbers(client):
    """Testing the encode route with seven numbers"""

    result = client.get("/encode/8756412")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "8B75S="}
    assert len(response_body["encoded"]) == 6


def test_encode_with_eight_numbers(client):
    """Testing the encode route with eight numbers"""

    result = client.get("/encode/99999999")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {"encoded": "2VBO7V"}
    assert len(response_body["encoded"]) == 6


def test_encode_with_nine_numbers(client):
    """
    Testing the encode route with nine numbers.
    It must return an error message as the max length is 8
    """

    result = client.get("/encode/123456789")

    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body == {
        "message": "The number must have a maximun of 8 characters"
    }


def test_decode_with_valid_parameter(client):
    """Testing the decode route with a valid code parameter"""

    result = client.get("/decode/2VBO7V")

    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert response_body == {
        "decoded": 99999999
    }
