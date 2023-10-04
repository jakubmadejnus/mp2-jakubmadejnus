from questions.sort_an_array import sortArray

import time

def test_sort_array():
    start_time = time.time()

    assert sortArray([5,2,3,1]) == [1,2,3,5]
    assert sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5]
    assert sortArray([]) == []
    assert sortArray([1]) == [1]
    assert sortArray([100, -100, 0]) == [-100, 0, 100]
    assert sortArray([5,5,5,5,5]) == [5,5,5,5,5]

    large_input = list(range(10**5, 0, -1))
    large_output = list(range(1, 10**5 + 1))
    assert sortArray(large_input) == large_output

    large_input = [10**5] * (10**5)
    large_output = [10**5] * (10**5)
    assert sortArray(large_input) == large_output

    alternating_input = [1, 10**5] * (10**5 // 2)
    alternating_output = [1] * (10**5 // 2) + [10**5] * (10**5 // 2)
    assert sortArray(alternating_input) == alternating_output

    end_time = time.time()
    assert end_time - start_time <= 2

test_sort_array()