"""
Dynamic Array Class
By: Suryakiran Santhosh
University of California, Davis

Purpose:
To better understand the Array Data Structures, I am building an Array from scratch in Python.
Eventually, will do the same in Javascript.
"""


class Array:

    def __init__(self, size):
        """
        member variables: array
        constructor creates an array of size length and assigns all indices with None
        """
        self.array = []
        self.length = 0

    def insert(self, value):
        """
        insert at the end of an array
        """
        self.array.append(value)

    def removeAt(self, index):
        """
        removes element at index and moves all elements to the right of the index one spot to the left
        """
        # check to see if index is in the array
        if (0 <= index < len(self.array)):
            del self.array[index]
        else:
            # throw an exception to warn user
            raise Exception("Index outside of array range.")

    def __str__(self):
        return str(self.array)
