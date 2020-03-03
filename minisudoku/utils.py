# Utility functions
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def increment_array(input_list: list, base: int) -> list:
    '''Increments a list of numbers for a given radix. Will not increment
    beyond the maximum representable value.

    EX: Base 2
       [0,0,0,0]
    -> [0,0,0,1]
    -> [0,0,1,0]
    -> [0,0,1,1]

    Args:
        input_list: Input list in the given radix.
        base: Radix of the number represented in ``input_list``

    Returns:
        Input_list after incrementation or ``input_list`` if max value.
    '''

    # Check for invalid radix
    if base < 2:
        raise ValueError(f"ERROR: Can't increment a number with base {base}.")

    # Check for invalid arrays
    if input_list is None:
        raise ValueError("ERROR: input_list is None. Can't increment.")

    for number in input_list:
        if number >= base:
            raise ValueError(f"ERROR: Found a number larger than or equal to the given radix!\
                A number of radix {base} can't equal or exceed that number. Can't increment.")

    # Check for maximum value
    if all(number == (base - 1) for number in input_list):
        eprint("WARN: Value at its maximum. Can't Increment.")
        return input_list

    ptr = len(input_list) - 1
    while input_list[ptr] == base - 1:
        input_list[ptr] = 0
        ptr -= 1
    input_list[ptr] += 1
    return input_list



def decrement_array(input_list: list, base: int) -> list:
    '''Decrements a list of numbers for a given radix. Will not decrement
    beyond 0.

    EX: Base 2
       [0,0,1,1]
    -> [0,0,1,0]
    -> [0,0,0,1]
    -> [0,0,0,0]

    Args:
        input_list: Input list in the given radix.
        base: Radix of the number represented in ``input_list``

    Returns:
        Input_list after decrementation or ``input_list`` if min value.
    '''

    # Check for invalid radix
    if base < 2:
        raise ValueError(f"ERROR: Can't decrement a number with base {base}.")

    # Check for invalid arrays
    if input_list is None:
        raise ValueError("ERROR: input_list is None. Can't decrement.")

    for number in input_list:
        if number >= base:
            raise ValueError(f"ERROR: Found a number larger than or equal to the given radix!\
                A number of radix {base} can't equal or exceed that number. Can't decrement.")

    # Check for maximum value
    if all(number == 0 for number in input_list):
        eprint("WARN: Value at its minimum. Can't decrement.")
        return input_list

    ptr = len(input_list) - 1
    while input_list[ptr] == 0:
        input_list[ptr] = base - 1
        ptr -= 1
    input_list[ptr] -= 1
    return input_list
