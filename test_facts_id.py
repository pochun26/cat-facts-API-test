
import pytest
import requests


base_url = "https://cat-fact.herokuapp.com"


def test_get_cat_fact_by_id():
    """
    GET /facts/:factID
    """
    response = requests.get(f"{base_url}/facts/63d91fa18bede8931dc75bd4")
    assert response.status_code == 200
    data = response.json()
    assert data["_id"] == "63d91fa18bede8931dc75bd4"
    assert data["text"] == "Cats are liquid)))."
    # https://www.stemfellowship.org/the-ig-nobel-prize-why-are-cats-liquid/


def test_non_exist_id():
    """
    GET /facts/:fake_factID
    """
    response = requests.get(f"{base_url}/facts/63d91fa18bede8931dc75bd5")
    assert response.status_code == 404
