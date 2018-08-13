"""

Beginner Series #3 Sum of Numbers

Given two integers a and b, which can be positive or negative, find the sum
of all the numbers between including them too and return it. If the two numbers
are equal return a or b.

Note: a and b are not ordered!

Examples
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

"""


def get_sum(a, b):
    # good luck!
    if a == b:
        return a
    elif a < b:
        x = sum(i for i in range(a, b + 1))
    else:
        x = sum(i for i in range(b, a + 1))
    return x


"""
Alternatively recursive functions could have been used
ie:

def get_sum(a,b):
    #good luck!
    if a == b:
        return a
    elif a < b:
        x = a + get_sum(a + 1, b)
    else:
        x = b + get_sum(b + 1, a)
    return x
"""
