from questions.kth_largest_element import KthLargest

def test_kth_largest():
    kthLargest1 = KthLargest([3, 1, 5, 12, 2, 11], 4)
    assert kthLargest1.add(6) == 5
    assert kthLargest1.add(13) == 6
    assert kthLargest1.add(4) == 6

    kthLargest2 = KthLargest([], 1)
    assert kthLargest2.add(1) == 1
    assert kthLargest2.add(2) == 2

    nums = [i for i in range(1, 10001)]
    kthLargest3 = KthLargest(nums, 5000)
    assert kthLargest3.add(10001) == 5002
    assert kthLargest3.add(10002) == 5003

    kthLargest4 = KthLargest([5, 5, 5, 5, 5], 2)
    assert kthLargest4.add(5) == 5
    assert kthLargest4.add(6) == 5
    assert kthLargest4.add(7) == 6
    
    kthLargest5 = KthLargest([8, 7, 6, 5, 4, 3, 2, 1], 1)
    assert kthLargest5.add(0) == 8
    assert kthLargest5.add(9) == 9
    
    kthLargest6 = KthLargest([1], 1)
    assert kthLargest6.add(1) == 1
    assert kthLargest6.add(2) == 2
