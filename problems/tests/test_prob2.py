import pytest
from problems.one_to_ten.prob_2 import calc_fib_term


class TestProb2:
    def test_calc_term(self):
        # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
        term_1 = 1
        assert calc_fib_term(1) == term_1
        term_2 = 2
        assert calc_fib_term(2) == term_2
        term_3 = 3
        assert calc_fib_term(3) == term_3
        term_4 = 5
        assert calc_fib_term(4) == term_4
        term_5 = 8
        assert calc_fib_term(5) == term_5
