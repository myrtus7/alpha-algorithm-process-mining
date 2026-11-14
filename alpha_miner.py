def alpha(log: set[set[str]]):
    pass

def define_all_events(log: set[tuple[str]]) -> set[str] :
    # using a tuple to keep order and repetition of activities
    # could also do a one-liner with return set().union(*log) but both are O(n)

    _validate_log(log)

    t_l = set()
    for trace in log :
        for activity in trace:
            t_l.add(activity)
    return t_l

def define_all_possible_start_events(log: set[tuple[str]]) -> set[str] :
    _validate_log(log)

    t_i = set()
    for trace in log:
        t_i.add(trace[0])
    return t_i

def define_all_possible_end_events(log: set[tuple[str]]) -> set[str] :
    _validate_log(log)

    t_o = set()
    for trace in log:
        t_o.add(trace[len(trace)-1])
    return t_o

def _validate_log(log: set[tuple[str, ...]]) -> None:
    if not log or any(len(trace) == 0 for trace in log):
        raise ValueError('invalid log')