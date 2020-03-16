import pytest
from problems.one_to_ten.prob_3 import find_primes


class TestProb3:
    def test_find_primes(self):
        # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
        assert find_primes(5) == [2, 3, 5]
        assert find_primes(10) == [2, 3, 5, 7]
