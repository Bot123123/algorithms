"""
    Sieve of Eratosthenes
    ---------------------
    Is a simple, ancient algorithm for finding all prime numbers
    up to any given limit. It does so by iteratively marking as composite
    (i.e. not prime) the multiples of each prime, starting with the multiples
    of 2.

    The sieve of Eratosthenes is one of the most efficient ways
    to find all of the smaller primes (below 10 million or so).

    Time Complexity: O(n log log n)

    Pseudocode: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def eratosthenes(end, start=2, return_boolean=False):
    """
    Finds all primes < `end`.

    :param end: An integer. The upper limit of the range to look for primes.
    :param start: An integer. The start of the range to look for primes.
    :param return_boolean: A boolean. Represents the type of return type.
    :rtype: Depending on `return_boolean` either returns boolean and primes or
            just the primes.
    """
    if start > end:
        return [] if not return_boolean else (False, [])

    sieve = range(end)
    primes = []
    next_num = 2

    while next_num:
        if start <= next_num < end:
            primes.append(next_num)

        for i in sieve[::next_num]:
            if i is not None:
                sieve[i] = None

        next_num = next((i for i in sieve[(next_num + 1):] if i is not None), None)

    if return_boolean:
        return bool(primes), primes
    return primes
