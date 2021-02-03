"""
Test File for DynamicArray
By: Suryakiran Santhosh
University of California, Davis

Purpose:
To better understand the Array Data Structures, I am building an Array from scratch in Python. 
Eventually, will do the same in Javascript.
"""


from ArrayDS import *


def main():
    array1 = Array(1)
    print(array1)  # prints empty list
    array1.insert("zero")
    array1.insert("first")
    print(array1)


if __name__ == "__main__":
    main()
