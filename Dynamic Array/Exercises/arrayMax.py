"""
Array Exercise 1
By: Suryakiran Santhosh

Create a method to return the largest number. What is the runtime complexity of this method?
"""


import random


def arrayMax(array: list) -> int:
    currentMax = array[0]
    for i in range(len(array) - 1):
        currentMax = max(currentMax, array[i])
    return currentMax


def main():
    # generate a list of number in the range of 0 to 10000000
    arr = list()
    for i in range(1000):
        arr.append(random.randint(0, 10000000))
    print(arrayMax(arr))


if __name__ == "__main__":
    main()
