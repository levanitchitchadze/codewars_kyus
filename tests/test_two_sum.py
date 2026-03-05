import pytest

from codewars_kyus.kyu_4.two_sum import two_sum

NUMS = [2, 7, 11, 15]


@pytest.mark.parametrize(
    "target,output", [
        (4, False),
        (7, False),
        (9, [0, 1]),
        (13, [0, 2]),
        (17, [0, 3]),
        (22, [1, 3]),
        (26, [2, 3]),
        (30, False),
    ]
)
def test_two_sum(target, output):
    assert two_sum(NUMS, target) == output
