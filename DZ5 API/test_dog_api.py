import pytest
import requests

BASE_URL = 'https://dog.ceo/api'


def test_list_all_breeds_200():
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    assert response.status_code == 200


def test_random_image():
    response = requests.get(f'{BASE_URL}/breeds/image/random')
    assert response.status_code == 200
    body = response.json()
    assert body['message'].startswith('https://images.dog.ceo/breeds/')


@pytest.mark.parametrize(
    ('breed', 'sub_breed'),
    [
        ('hound', 'afghan'),
        ('bulldog', 'french'),
        ('retriever', 'golden'),
    ],
)
def test_sub_breeds_list(breed, sub_breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/list')
    assert response.status_code == 200
    assert sub_breed in response.json()['message']


@pytest.mark.parametrize(
    ('breed', 'count'),
    [
        ('akita', 1),
        ('pug', 3),
        ('boxer', 5),
    ],
)
def test_random_images_by_breed(breed, count):
    response = requests.get(f'{BASE_URL}/breed/{breed}/images/random/{count}')
    assert response.status_code == 200
    images = response.json()['message']
    assert len(images) == count
    assert all(f'/breeds/{breed}' in image for image in images)


def test_unknown_breed_returns_404():
    response = requests.get(f'{BASE_URL}/breed/notabreed/images')
    assert response.status_code == 404
    assert response.json()['status'] == 'error'
