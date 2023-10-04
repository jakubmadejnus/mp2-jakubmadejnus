from questions.search_min_diff_element import find_min_difference_element

from random import randint, seed
from time import time

def brute_force_min_difference(nums, key):
    return min(nums, key=lambda x: (abs(x - key), x))

def test_find_min_difference_element():
    # Basic Examples
    assert find_min_difference_element([4, 6, 10], 7) == 6
    assert find_min_difference_element([4, 6, 10], 4) == 4
    assert find_min_difference_element([1, 3, 8, 10, 15], 12) == 10
    assert find_min_difference_element([4, 6, 10], 17) == 10

    # More Complex Cases
    assert find_min_difference_element([1, 3, 8, 10, 15, 20, 25, 30], 18) == 20
    assert find_min_difference_element([5, 10, 15, 25, 35, 45, 50, 55, 60], 48) == 50
    assert find_min_difference_element([10, 15, 20, 25, 30, 40, 50, 55, 60, 70, 80, 90, 100], 85) == 80

    # Large Input for Efficiency Testing
    seed(42)  # to make it reproducible
    large_nums = sorted([randint(1, 100000) for _ in range(10000)])
    large_key = randint(1, 100000)

    # Check for time efficiency
    start_time = time()
    result = find_min_difference_element(large_nums, large_key)
    end_time = time()
    assert (end_time - start_time) < 0.1  # should run within a fraction of a second for logN

    # Validate result with brute force
    expected = brute_force_min_difference(large_nums, large_key)
    assert result == expected

    # Test cases with keys on both ends of the range
    assert find_min_difference_element([1, 2, 3, 4, 5], 0) == 1
    assert find_min_difference_element([1, 2, 3, 4, 5], 6) == 5
