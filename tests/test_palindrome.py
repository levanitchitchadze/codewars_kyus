import pytest

from codewars_kyus.kyu_5.palindrome import palindrome


@pytest.mark.parametrize(
    "string,output", [
        ("level", True),
        ("Help", False),
        ("Ana", True),
        ("cotton", False),
        ("Mom", True),
        ("Kayak", True),
    ]
)
def test_palindrome(string: str, output: bool):
    assert palindrome(string) == output
