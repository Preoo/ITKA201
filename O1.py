from functools import partial, reduce
from typing import List, Tuple

"""
Write a program to count how many numbers in a list falls within given range
[a,b]. Generate a list of random numbers and count how many of them falls into
following ranges: [0,10], [50,100] and [67,75].

"""

def build_pred(lower: int, upper: int, *args, func=None):
    def inclusive_range(lower_bound, upper_bound, value):
        return 1 if lower_bound <= value and value <= upper_bound else 0

    if func:
        return partial(func, lower, upper)

    return partial(inclusive_range, lower, upper)

def count_numbers_between_range(lower_upper_range: Tuple[int, int], \
                                list_of_random_ints: List[int], \
                                range_func_partial=None) -> int:

    pred = build_pred(*lower_upper_range, func=range_func_partial)
    return reduce(lambda total, n: total + pred(n), list_of_random_ints, 0)

if __name__ == "__main__":
    from random import randint
    n = 5
    _random_number_list = [randint(0, 100) for _ in range(n)]
    _ranges = ((0, 10), (50, 100), (67, 75))

    for _range in _ranges:
        # you could call following tested function
        # v = count_numbers_between_range(_range, _random_number_list)
        # OR this one-liner :)
        v = reduce(lambda total, s: total + int(_range[0] < s and s < _range[1]), \
                _random_number_list, 0)
        print(f'Out of random numbers {_random_number_list}, {v} fell in range {_range}')
