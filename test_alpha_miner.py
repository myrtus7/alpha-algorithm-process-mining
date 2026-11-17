import pytest
from alpha_miner import (alpha,
    define_all_events,
    define_all_possible_end_events,
    define_all_possible_start_events,
    _get_all_successions,
    _footprint_matrix)

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

@pytest.mark.parametrize("log,expected", [
    (LOG, {'a':{'b','e'}, 'b':{'c'}, 'c':{'d','e'}, 'e':{'c','d'}}),
    ({('a',)}, {}),
    ({('a',), ('a', 'b')}, {'a':{'b'}}),
])
def test_get_all_successions(log, expected):
    assert _get_all_successions(log) == expected

LOG_PARALLEL = {('a', 'b', 'c', 'd'), ('a', 'c', 'b', 'd')}

@pytest.mark.parametrize("log, expected", [
    ({('a',)}, [['#']]),
    # events sorted: a, b
    ({('a',), ('a', 'b')}, [
        ['#',  '->'],
        ['<-', '#' ],
    ]),
    # events sorted: a, b, c, d, e
    (LOG, [
        ['#',  '->', '#',  '#',  '->'],
        ['<-', '#',  '->', '#',  '#' ],
        ['#',  '<-', '#',  '->', '||'],
        ['#',  '#',  '<-', '#',  '<-'],
        ['<-', '#',  '||', '->', '#' ],
    ]),
    # events sorted: a, b, c, e
    (LOG_DIFFERENT_START_END, [
        ['#',  '->', '#',  '#' ],
        ['<-', '#',  '->', '#' ],
        ['#',  '<-', '#',  '->'],
        ['#',  '#',  '<-', '#' ],
    ]),
    # events sorted: a, b, c, d
    (LOG_PARALLEL, [
        ['#',  '->', '->', '#' ],
        ['<-', '#',  '||', '->'],
        ['<-', '||', '#',  '->'],
        ['#',  '<-', '<-', '#' ],
    ]),
])
def test_footprint_matrix(log, expected):
    events = sorted(define_all_events(log))
    assert _footprint_matrix(log, events) == expected

@pytest.mark.parametrize("invalid_log", [
    None,
    set(),
    {()},
])
def test_alpha_for_invalid_input(invalid_log):
    with pytest.raises(ValueError):
        alpha(invalid_log)
