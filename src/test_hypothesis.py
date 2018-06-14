from hypothesis import given  # define the inputs
import hypothesis.strategies as st
import division

@given(k = st.integers(min_value=1)) # main decorator
def test_divisible_by_11(k):
    assert division.divisible_by_11_best(11*k)