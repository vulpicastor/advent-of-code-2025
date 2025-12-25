#!/usr/bin/env python3

import numpy as np
import aocd

YEAR = 2025
DAY = 1


def parse_input(lines):
    steps = [50]
    for l in lines:
        n = int(l[1:])
        steps.append(n if l[0] == 'R' else -n)
    return steps


def count_zeros(steps):
    print(np.cumsum(steps) % 100)
    return np.sum((np.cumsum(steps) % 100) == 0)


def count_zero_passes(steps):
    state = 0
    zeros = 0
    prev_zero = False
    for n in steps:
        state += n
        quotient, modulus = np.divmod(state, 100)
        if modulus == 0:
            zeros += quotient if quotient > 0 else abs(quotient) + 1
            prev_zero = True
        elif prev_zero:
            zeros += quotient if quotient >= 0 else abs(quotient + 1)
            prev_zero = False
        else:
            zeros += abs(quotient)
        state = modulus
    return zeros


def main():
    data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    data = aocd.get_data(day=DAY, year=YEAR)
    inlist = [l for l in data.split('\n') if l]  # noqa: F841

    steps = parse_input(inlist)
    answer = count_zeros(steps)
    print(answer)
    aocd.submit(answer, part='a', day=DAY, year=YEAR)

    answer = count_zero_passes(steps)
    print(answer)
    aocd.submit(answer, part='b', day=DAY, year=YEAR)


if __name__ == '__main__':
    main()
