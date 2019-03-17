"""

Primes in numbers

Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"

"""


def primeFactors(n):
    primes = []
    i = 2
    while i * i < n or i <= n:
        first_time = True
        while n % i == 0:
            n = n / i
            if first_time:
                primes.append([i, 1])
                first_time = False
            else:
                primes[-1][1] += 1
        i = i + 1

    return "".join(["(%d**%d)" % (a[0], a[1]) if a[1] > 1 else "(%d)" % (a[0]) for a in primes])
