import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_list_posts_200():
    response = requests.get(f'{BASE_URL}/posts')
    assert response.status_code == 200


@pytest.mark.parametrize(
    ('resource', 'expected_count'),
    [
        ('posts', 100),
        ('comments', 500),
        ('users', 10),
    ],
)
def test_resource_count(resource, expected_count):
    response = requests.get(f'{BASE_URL}/{resource}')
    assert response.status_code == 200
    assert len(response.json()) == expected_count


@pytest.mark.parametrize(
    ('resource', 'item_id'),
    [
        ('posts', 1),
        ('albums', 50),
        ('users', 10),
    ],
)
def test_get_item_by_id(resource, item_id):
    response = requests.get(f'{BASE_URL}/{resource}/{item_id}')
    assert response.status_code == 200
    assert response.json()['id'] == item_id


def test_post_comments():
    response = requests.get(f'{BASE_URL}/posts/1/comments')
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_missing_post_returns_404():
    response = requests.get(f'{BASE_URL}/posts/67676767')
    assert response.status_code == 404
