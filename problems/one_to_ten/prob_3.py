from typing import List

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def find_primes(n: int) -> List[int]:
    if n < 2:
        return [1]
    elif n == 2:
        return [1, 2]
    p = 2
    numbers = [i for i in range(2, n + 1)]
    for p in range(2, n + 1):
        if p in numbers:
            for i in range(n + 1):
                r = p * (p + i)
                if r in numbers:
                    numbers.remove(r)
    return numbers


def solution():
    num = 600851475143
    primes = find_primes(int(num / 2))
    rev_primes = primes.reverse()
    for i in rev_primes:
        if num % i == 0:
            return num

