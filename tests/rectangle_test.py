from src.rectangle import Rectangle
import pytest

@pytest.mark.parametrize(
    ('side_a', 'side_b', 'area', 'perimeter'),
    [
        pytest.param(3, 5, 15, 16, id='integer'),
        pytest.param(3.5, 5.5, 19.25, 18.0, id='float'),
    ]

)
def test_rectangle_area_and_perimeter(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'Area of rectangle with sides {side_a} and {side_b} should be {area}, actual is {r.area}'
    assert r.perimeter == perimeter, f'Perimeter of rectangle with sides {side_a} and {side_b} should be {perimeter}, actual is {r.perimeter}'
