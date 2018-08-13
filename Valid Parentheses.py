"""

Valid Parentheses

Write a function called that takes a string of parentheses, and determines if
the order of the parentheses is valid. The function should return true if the
string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid
ASCII characters. Furthermore, the input string may be empty and/or not contain
any parentheses at all. Do not treat other forms of brackets as parentheses
(e.g. [], {}, <>).

"""


def valid_parentheses(string):
    # your code here
    number_of_opn = 0
    number_of_cls = 0
    for x in string:
        if x == "(":
            number_of_opn += 1
        if x == ")":
            number_of_cls += 1
        if number_of_cls > number_of_opn:
            return False
    if number_of_opn == number_of_cls:
        return True
    return False
