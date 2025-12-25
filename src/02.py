#!/usr/bin/env python3

# ruff: noqa: F401
import collections
import functools
import io
import itertools
import operator as op
import re
import timeit

import numpy as np
import aocd

YEAR = 2025
DAY = 2


def invalid(x):
    s =  str(x)
    if (n := len(s)) % 2:
        return False # n is odd.
    else:
        return s[:n // 2] == s[n // 2:]


def invalid2(x):
    s = str(x)
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i:
            continue
        if re.fullmatch(f'({s[:i]})+', s):
            return True
    return False


def check_range(a, b, invalid_method=invalid):
    l = [i for i in range(a, b + 1) if invalid_method(i)]
    print(l)
    return l


def main():
    data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
    data = aocd.get_data(day=DAY, year=YEAR)
    inlist = [tuple(map(int, l.split('-'))) for l in data.split(',') if l]  # noqa: F841

    answer = sum(sum(check_range(*x)) for x in inlist)
    print(answer)
    # aocd.submit(answer, part='a', day=DAY, year=YEAR)

    answer = sum(sum(check_range(*x, invalid_method=invalid2)) for x in inlist)
    print(answer)
    aocd.submit(answer, part='b', day=DAY, year=YEAR)


if __name__ == '__main__':
    main()
