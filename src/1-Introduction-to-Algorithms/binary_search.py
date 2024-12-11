from typing import Any
from collections.abc import Iterable


# Stupid way to find a value in a list
# "Brutal force" algorithm
# In some cases it will be necessary to go through the entire list,
# in a very large list it will be inefficient - Big O -> O(n)
def _search(array: Iterable, value: Any) -> float | None:
    index = 0
    for item in array:
        if item == value:
            return index
        else:
            index += 1
    return None


# Big O -> O(log(2)n)
def binary_search(
        array: Iterable, value: Any) -> float | None:
    low = 0
    high = len(list(array)) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list(array)[mid]
        if guess == value:
            return mid
        if guess > value:
            high = mid - 1
        if guess < value:
            low = mid + 1
    return None


def main():
    numbers = [n for n in range(1000000)]
    print('(index, steps)')
    print(_search(numbers, 999999))
    print(binary_search(numbers, 999999))


if __name__ == '__main__':
    main()