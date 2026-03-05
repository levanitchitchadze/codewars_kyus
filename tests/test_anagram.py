import pytest

from codewars_kyus.kyu_7.anagram import anagram


@pytest.mark.parametrize(
    "s1,s2,output",
    [
        ("horror", "rorroh", True),
        ("cinematographer", "megachiropteran", True),
        ("jack", "sparrow", False)
    ]
)
def test_anagram(s1, s2, output):
    assert anagram(s1, s2) == output
