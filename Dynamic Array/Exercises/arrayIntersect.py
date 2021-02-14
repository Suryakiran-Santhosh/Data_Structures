"""
Array Exercise 1
By: Suryakiran Santhosh

Create a method to return the common items in this array and another array.
"""


import random


def arrayIntersection(array1: list, array2: list) -> list:
    """
    # Brute Force Nested For Loop Method
    # double for loop leads to O(n^2)
    result = list()
    for i in array1:
        for j in array2:
            if i == j:
                result.append(i)
    """

    # set method
    set1 = set(array1)
    set2 = set(array2)
    return(list(set1.intersection(set2)))


def main():
    arr1 = list()
    arr2 = list()
    for i in range(1000):
        arr1.append(random.randint(0, 1000000))
        arr2.append(random.randint(0, 1000000))
    print(arrayIntersection(arr1, arr2))


if __name__ == "__main__":
    main()
