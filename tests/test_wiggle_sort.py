from questions.wiggle_sort import wiggleSort

def test_wiggle_sort():
    nums = [3,5,2,1,6,4]
    wiggleSort(nums)
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            assert nums[i] <= nums[i+1]
        else:
            assert nums[i] >= nums[i+1]

    nums = [6,6,5,6,3,8]
    wiggleSort(nums)
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            assert nums[i] <= nums[i+1]
        else:
            assert nums[i] >= nums[i+1]

    # Testing efficiency with large inputs
    nums = list(range(5 * 10**4))
    wiggleSort(nums)
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            assert nums[i] <= nums[i+1]
        else:
            assert nums[i] >= nums[i+1]

    # Testing with repeated large numbers
    nums = [10**4] * (5 * 10**4)
    wiggleSort(nums)
    for i in range(len(nums) - 1):
        if i % 2 == 0:
            assert nums[i] <= nums[i+1]
        else:
            assert nums[i] >= nums[i+1]
