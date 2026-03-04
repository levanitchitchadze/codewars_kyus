import pytest

from codewars_kyus.kyu_2.descending_order import descending_order


@pytest.mark.parametrize(
    "input, output", [
        (0, 0),
        (15, 51),
        (123456789, 987654321),
        (135142, 543211)
    ]
)
def test_descending_order(input, output):
    assert descending_order(input) == output
