import pytest
from alpha_miner import define_all_events

@pytest.mark.parametrize("logs, expected", [
    ({('a')}, {'a'}),
    ({('a','b','c','d'),('a','e','c','d'),('a','e','d'), ('a','e','c','e','c','d')}, {'a','b','c','d','e'})
])
def test_define_all_events(logs, expected):
    assert define_all_events(logs) == expected

@pytest.mark.parametrize("invalid_log", [
    None, 
    set(),
    {()},
])
def test_define_all_events_for_invalid_input(invalid_log):
    with pytest.raises(ValueError):
        define_all_events(invalid_log)
