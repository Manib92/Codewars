"""

Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

Find the unique number (this kata)
Find the unique string
Find The Unique

"""


def find_uniq(arr):
    # your code here
    set_arr = set(arr)
    new_set = []
    for i in set_arr:
        total = sum(1 for j in arr if i == j)
        if total <= 1:
            new_set.append(i)

    return new_set[0]   # n: unique integer in the array


"""
Below you will find the code for the best solution for the task. The reason I
did not do something similar to that was because in the code below they made the
assumption that there was only 2 possible unique numbers within the array:

def find_uniq(arr):
    # your code here
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
