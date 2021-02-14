"""
Array Exercise 1
By: Suryakiran Santhosh

Create a method to reverse the array. For example, if the array includes [1, 2, 3, 4], after reversing and printing it, we should see [4, 3, 2, 1].
"""


import random


def arrayReverse(array1: list) -> list:
    reverseList = list()
    for i in range(len(array1) - 1, 0, -1):
        reverseList.append(array1[i])
    return reverseList


def check(order: list, reverse: list) -> bool:
    """
    checks to see if one array is the reverse of the other
    """
    ans = list()
    if len(order) == len(reverse):
        for i in range(len(order)):
            if (order[i] == reverse[(len(reverse) - 1) - i]):
                ans.append(True)
            else:
                ans.append(False)
    return(False not in ans)


def main():
    # generate a list of number in the range of 0 to 10000000
    arr = list()
    for i in range(1000):
        arr.append(random.randint(0, 10000000))
    ans = arrayReverse(arr)
    print(check(arr, ans))


if __name__ == "__main__":
    main()
