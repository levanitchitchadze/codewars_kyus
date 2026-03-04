import pytest

from codewars_kyus.kyu_3.highest_and_lowest import high_and_low


@pytest.mark.parametrize(
    "input_str, expected_output", [
        ("8 3 -5 42 -1 0 0 -9 4 7 4 -4", "42 -9"),
        ("1 2 3", "3 1"),
        ("10 10 10", "10 10"),
        ("-1 -1 -1", "-1 -1")]
)
def test_high_and_low(input_str, expected_output):
    assert high_and_low(input_str) == expected_output
