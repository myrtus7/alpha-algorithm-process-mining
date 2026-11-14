import pytest
from alpha_miner import (define_all_events,
    define_all_possible_end_events,
    define_all_possible_start_events)

LOG = {
    ('a', 'b', 'c', 'd'),
    ('a', 'e', 'c', 'd'),
    ('a', 'e', 'd'),
    ('a', 'e', 'c', 'e', 'c', 'd'),
}

LOG_DIFFERENT_START_END = {('a', 'b', 'c'), ('b', 'c', 'e')}

@pytest.mark.parametrize("logs, expected", [
    ({('a')}, {'a'}),
    (LOG, {'a','b','c','d','e'})
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

@pytest.mark.parametrize("log, expected", [
    ({('a')}, {'a'}),                              
    ({('a','b','c')}, {'a'}),            
    (LOG, {'a'}),
    (LOG_DIFFERENT_START_END, {'a','b'})
])
def test_define_all_possible_start_events(log, expected):
    assert define_all_possible_start_events(log) == expected

@pytest.mark.parametrize("log, expected", [
    ({('a')}, {'a'}),                              
    ({('a','b','c')}, {'c'}),          
    (LOG, {'d'}),
    (LOG_DIFFERENT_START_END, {'c', 'e'})
])
def test_define_all_possible_end_events(log, expected):
    assert define_all_possible_end_events(log) == expected