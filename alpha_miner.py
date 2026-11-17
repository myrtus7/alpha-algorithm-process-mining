from collections import defaultdict

type Trace = tuple[str, ...]
type Log = set[Trace]
type Matrix = list[list[str]]

def alpha(log: Log):
    _validate_log(log)

def define_all_events(log: Log) -> set[str] :
    # using a tuple to keep order and repetition of activities
    # could also do a one-liner with return set().union(*log) but both are O(n)
    t_l = set()
    for trace in log :
        for activity in trace:
            t_l.add(activity)
    return t_l

def define_all_possible_start_events(log: Log) -> set[str] :
    t_i = set()
    for trace in log:
        t_i.add(trace[0])
    return t_i

def define_all_possible_end_events(log: Log) -> set[str] :
    t_o = set()
    for trace in log:
        t_o.add(trace[len(trace)-1])
    return t_o

def _footprint_matrix(log: Log, events: list[str]) -> Matrix:
    n = len(events)
    matrix = [['#' for j in range(n)] for i in range(n)]
    _fill_matrix_with_successions(matrix,events,log)
    _fill_matrix_with_inverse_causalities_parallelism(matrix)
    return matrix
        

def _fill_matrix_with_successions(matrix: Matrix, events:list[str], log: Log) -> None :
    successions = _get_all_successions(log)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if j != i and events[j] in successions[events[i]]:
                matrix[i][j] = '->'


def _fill_matrix_with_inverse_causalities_parallelism(matrix: Matrix) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '->' or matrix[i][j]=='||':
                if matrix[j][i] == '->':
                    matrix[j][i] = '||'
                else:
                    matrix[j][i] = '<-'
    

def _get_all_successions(log: Log) -> defaultdict[str, set[str]]:
    successions = defaultdict(set)
    for trace in log:
        n = len(trace)
        for i in range(n-1):
            successions[trace[i]].add(trace[i+1])

    return successions

def _validate_log(log: Log) -> None:
    if not log or any(len(trace) == 0 for trace in log):
        raise ValueError('invalid log')