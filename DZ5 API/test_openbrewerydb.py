import pytest
import requests

BASE_URL = 'https://api.openbrewerydb.org/v1/breweries'


def test_list_breweries_200():
    response = requests.get(BASE_URL)
    assert response.status_code == 200


def test_random_brewery():
    response = requests.get(f'{BASE_URL}/random')
    assert response.status_code == 200
    assert len(response.json()) == 1


@pytest.mark.parametrize(
    ('brewery_type', 'per_page'),
    [
        ('micro', 5),
        ('brewpub', 3),
        ('regional', 2),
    ],
)
def test_breweries_by_type(brewery_type, per_page):
    response = requests.get(BASE_URL, params={'by_type': brewery_type, 'per_page': per_page})
    assert response.status_code == 200
    assert len(response.json()) == per_page


@pytest.mark.parametrize(
    ('state', 'per_page'),
    [
        ('california', 5),
        ('new_york', 3),
        ('texas', 2),
    ],
)
def test_breweries_by_state(state, per_page):
    response = requests.get(BASE_URL, params={'by_state': state, 'per_page': per_page})
    assert response.status_code == 200
    assert len(response.json()) == per_page


def test_unknown_brewery_returns_404():
    response = requests.get(f'{BASE_URL}/notabrewery')
    assert response.status_code == 404
