from questions.search_rotated_array import search_rotated_array

import time

def test_search_rotated_array():
    assert search_rotated_array([10, 15, 1, 3, 8], 15) == 1
    assert search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10) == 4

    assert search_rotated_array([10, 15, 20, 25, 1, 3, 8], 8) == 6
    assert search_rotated_array([5, 6, 7, 8, 9, 10, 1, 2, 3], 3) == 8

    large_nums = [i for i in range(1000, 10000)] + [i for i in range(0, 1000)]
    assert search_rotated_array(large_nums, 9999) == 8999
    assert search_rotated_array(large_nums, 500) == 9500
    assert search_rotated_array(large_nums, 10) == 9010

    assert search_rotated_array([1], 1) == 0
    assert search_rotated_array([1], 0) == -1
    assert search_rotated_array([4, 5, 6, 1, 2, 3], 0) == -1

    TIME_LIMIT = 0.1  # set to 100 milliseconds

    large_nums = [i for i in range(100000, 1000000)] + [i for i in range(0, 100000)]

    start_time = time.time()

    assert search_rotated_array(large_nums, 999999) == 899999
    assert search_rotated_array(large_nums, 50000) == 950000
    assert search_rotated_array(large_nums, 100) == 900100

    end_time = time.time()

    assert end_time - start_time < TIME_LIMIT
