import pytest
import division


def test_divisible_by_11():
    for k in range(10):
        assert division.divisible_by_11(11*k)
        assert division.divisible_by_11(121)
        assert division.divisible_by_11(12122)