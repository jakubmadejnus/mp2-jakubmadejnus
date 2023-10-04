from questions.count_rotations import count_rotations

def test_count_rotations():

    assert count_rotations([10, 15, 1, 3, 8]) == 2
    assert count_rotations([4, 5, 7, 9, 10, -1, 2]) == 5
    assert count_rotations([1, 3, 8, 10]) == 0

    assert count_rotations([15, 20, 25, 1, 3, 8, 10]) == 3
    assert count_rotations([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 5

    # Large Input for Efficiency Testing
    large_nums = [i for i in range(1000, 10000)] + [i for i in range(0, 1000)]
    assert count_rotations(large_nums) == 9000

    # Edge Cases
    assert count_rotations([1]) == 0
    assert count_rotations([2, 1]) == 1
    assert count_rotations([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
