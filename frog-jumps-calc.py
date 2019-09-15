#!/usr/bin/env python
"""
    File name: frog-jumps-calc.py
    Author: Dmitry Tsuprunov
    Date created: September 14, 2019
    Python Version: 3.7
"""
import sys


def memo(fn):
    """
    Memoizing all the things
    """
    cache = {}

    def memo_fn(*args):
        cached_val = cache.get(args)
        if cached_val:
            return cached_val
        cached_val = fn(*args)
        cache[args] = cached_val
        return cached_val

    return memo_fn


def possible_jumps(distance, jumps_made=0):
    """
    Calculates total number of jumps for all possible paths
    """
    if distance == 0:
        return jumps_made
    total_jumps = 0
    for i in range(distance):
        total_jumps += memo_possible_jumps(i, jumps_made + 1.0)
    return total_jumps


memo_possible_jumps = memo(possible_jumps)


def possible_paths(distance):
    """
    Calculating total number of possible paths
    """
    if distance == 0:
        return 1.0
    total = 0
    for i in range(distance):
        total += memo_possible_paths(i)
    return total


memo_possible_paths = memo(possible_paths)


def expected_jumps(distance):
    if distance == 0:
        return 0
    return possible_jumps(distance) / possible_paths(distance)


if __name__ == "__main__":
    try:
        arg = int(sys.argv[1])
    except:
        arg = 10
    for i in range(1, arg + 1):
        num_expected_jumps = expected_jumps(i)
        # uncomment line below to make sure that expected number of jumps
        # is equal to (distance + 1) / 2
        # tested up to a distance of 498 jumps
        # vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        # if (float(i)+1)/2 != num_expected_jumps:
        #     print('', i, num_expected_jumps)
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        # This line will print all values for all paths up to selected number
        # Feel free to test with >>> python3 frog-jumps-calc.py {distance}
        num_possible_paths = possible_paths(i)
        num_possible_jumps = possible_jumps(i)
        print(f"For a distance {i} there're {num_possible_paths} possible paths "
              f"containing {num_possible_jumps} jumps "
              f"with expected jumps equal to {num_expected_jumps}.")
