def alpha(log: set[set[str]]):
    pass

def define_all_events(log: set[tuple[str]]) -> set[str] :
    # using a tuple to keep order and repetition of activities
    # could also do a one-liner with return set().union(*log) but both are O(n)

    if not log or log == {()} or len(log) == 0:
        raise ValueError('null or empty log') 


    t_l = set()
    for trace in log :
        for activity in trace:
            t_l.add(activity)
    return t_l
