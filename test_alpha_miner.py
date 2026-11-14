import pytest
from alpha_miner import define_all_events

@pytest.mark.parametrize("logs, expected", [
    (set(), set()),
    ({()}, set()),
    ({('a')}, {'a'}),
    ({('a','b','c','d'),('a','e','c','d'),('a','e','d'), ('a','e','c','e','c','d')}, {'a','b','c','d','e'})
])
def test_define_all_events(logs, expected):
    assert define_all_events(logs) == expected