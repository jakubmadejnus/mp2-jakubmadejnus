from questions.find_sum_of_elements import find_sum_between_elements

def test_find_sum_between_elements():
    assert find_sum_between_elements([1, 3, 12, 5, 15, 11], 3, 6) == 23
    assert find_sum_between_elements([3, 5, 8, 7], 1, 4) == 12
    assert find_sum_between_elements([5], 1, 1) == 0  # Single element array
    assert find_sum_between_elements([5, 7], 1, 2) == 0  # Two element array
    assert find_sum_between_elements([3, 1, 2], 1, 2) == 0  # Test with out-of-order array
    assert find_sum_between_elements([5, 7, 9, 3, 1], 2, 5) == 12  # Sum excluding smallest and largest elements

    nums = [i for i in range(10**6, 0, -1)]
    k1 = 1000
    k2 = 5000
    expected_sum = sum(range(k1+1, k2))
    assert find_sum_between_elements(nums, k1, k2) == expected_sum

    k1 = 500000
    k2 = 600000
    expected_sum = sum(range(k1+1, k2))
    assert find_sum_between_elements(nums, k1, k2) == expected_sum

    # Test 4: Extremely large numbers with smaller k1 and k2 values
    nums = [i for i in range(10**6, 0, -1)] + [10**9, 10**9 + 1]
    k1 = 1
    k2 = 1000002
    expected_sum = 501000499999
    assert find_sum_between_elements(nums, k1, k2) == expected_sum
