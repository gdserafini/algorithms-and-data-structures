from typing import Any
from collections.abc import Iterable


# Stupid way to find a value in a list
# "Brutal force" algorithm
# In some cases it will be necessary to go through the entire list,
# in a very large list it will be inefficient
def search(array: Iterable, value: Any) -> tuple | None:
    index = 0
    op = 0
    for item in array:
        op = op + 1
        if item == value:
            return index, op
        else:
            index += 1
    return None


def binary_search(array: Iterable, value: Any) -> tuple | None:
    low = 0
    high = len(list(array)) - 1
    op = 0
    while low <= high:
        op = op + 1
        mid = (low + high) // 2
        guess = list(array)[mid]
        if guess == value:
            return mid, op
        if guess > value:
            high = mid - 1
        if guess < value:
            low = mid + 1
    return None


def main():
    numbers = [n for n in range(1000000)]
    print('(index, steps)')
    print(search(numbers, 999999))
    print(binary_search(numbers, 999999))


if __name__ == '__main__':
    main()