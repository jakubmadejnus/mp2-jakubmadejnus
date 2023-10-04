from typing import List

def verify_preorder(preorder: List[int]) -> bool:
    stack = []
    lower_bound = float('-inf')
    for num in preorder:
        if num < lower_bound:
            return False
        while stack and num > stack[-1]:
            lower_bound = stack.pop()
        stack.append(num)
    return True


def test_verify_preorder():
    assert verify_preorder([5,2,1,3,6]) == True
    assert verify_preorder([5,2,6,1,3]) == False
    assert verify_preorder([8, 4, 2, 1, 5, 7, 12, 10, 15]) == True
    assert verify_preorder([8, 4, 2, 1, 6, 12, 10, 5, 15]) == False
    assert verify_preorder([10, 9, 8, 7, 15, 12, 11, 13, 20]) == True
    assert verify_preorder([10, 9, 8, 7, 12, 6, 15]) == False

    # Additional Test: Extremely Large Test
    large_increasing_preorder = list(range(1, 10001))
    assert verify_preorder(large_increasing_preorder) == True

    large_mixed_preorder = [10_000] + list(range(1, 10_000))
    assert verify_preorder(large_mixed_preorder) == True
