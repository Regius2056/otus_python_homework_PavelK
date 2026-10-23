import pytest
from src.triangle import Triangle
@pytest.mark.parametrize(
    ('side_a', 'side_b', 'side_c', 'area', 'perimeter'),
    [
        pytest.param(3, 4, 5, 6, 12, id='integer'),
        pytest.param(2.5, 2.5, 2.5, 2.7063, 7.5, id='float'),
    ],
)
def test_triangle_area_and_perimeter(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == pytest.approx(area, rel=1e-4), (
        f'Area of triangle with sides {side_a}, {side_b}, {side_c} should be {area}, actual is {t.area}'
    )
    assert t.perimeter == pytest.approx(perimeter), (
        f'Perimeter of triangle with sides {side_a}, {side_b}, {side_c} should be {perimeter}, actual is {t.perimeter}'
    )
