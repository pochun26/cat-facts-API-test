
import pytest
import requests


base_url = "https://cat-fact.herokuapp.com"


def test_get_random_cat_fact():
    response = requests.get(f"{base_url}/facts/random")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "cat"
    assert isinstance(data["text"], str)


def test_cat_type():
    response = requests.get(f"{base_url}/facts/random?animal_type=cat")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "cat"
    assert isinstance(data["text"], str)


def test_dog_type():
    response = requests.get(f"{base_url}/facts/random?animal_type=dog")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "dog"
    assert isinstance(data["text"], str)


def test_two_type():
    response = requests.get(f"{base_url}/facts/random?animal_type=cat,dog")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "cat" or data["type"] == "dog"
    assert isinstance(data["text"], str)


def test_empty_type():
    response = requests.get(f"{base_url}/facts/random?animal_type=")
    assert response.status_code == 200
    data = response.json()
    assert data["type"] == "cat"
    assert isinstance(data["text"], str)
