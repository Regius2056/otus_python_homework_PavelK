import pytest
from src.square import Square
@pytest.mark.parametrize(
    ('side_a', 'area', 'perimeter'),
    [
        pytest.param(5, 25, 20, id='integer'),
        pytest.param(3.5, 12.25, 14.0, id='float'),
    ],
)
def test_square_area_and_perimeter(side_a, area, perimeter):
    s = Square(side_a)
    assert s.area == area, f'Area of square with side {side_a} should be {area}, actual is {s.area}'
    assert s.perimeter == perimeter, (
        f'Perimeter of square with side {side_a} should be {perimeter}, actual is {s.perimeter}'
    )
