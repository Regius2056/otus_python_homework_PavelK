import math
import pytest
from src.circle import Circle
@pytest.mark.parametrize(
    ('radius', 'area', 'perimeter'),
    [
        pytest.param(5, 78.5398, 31.4159, id='integer'),
        pytest.param(2.5, 19.6350, 15.7080, id='float'),
    ],
)
def test_circle_area(radius, area, perimeter):
    c = Circle(radius)
    assert c.area == pytest.approx(area, rel=1e-4), (
        f'Area of circle with radius {radius} should be {area}, actual is {c.area}'
    )
    assert c.perimeter == pytest.approx(perimeter, rel=1e-4), (
        f'Perimeter of circle with radius {radius} should be {perimeter}, actual is {c.perimeter}'
    )
