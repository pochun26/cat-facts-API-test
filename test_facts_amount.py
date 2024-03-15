
import pytest
import requests


base_url = "https://cat-fact.herokuapp.com"


def test_get_cat_fact_amount_1():
    response = requests.get(f"{base_url}/facts/random?amount=1")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert isinstance(data["text"], str)


def test_get_cat_fact_amount_2():
    response = requests.get(f"{base_url}/facts/random?amount=2")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    for d in data:
        assert isinstance(d["text"], str)


def test_get_cat_fact_amount_500():
    response = requests.get(f"{base_url}/facts/random?amount=500")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 500


def test_get_cat_fact_amount_0():
    response = requests.get(f"{base_url}/facts/random?amount=0")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_get_cat_fact_amount_501():
    response = requests.get(f"{base_url}/facts/random?amount=501")
    assert response.status_code == 405
