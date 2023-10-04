from questions.tree_distances_one import TreeNode, upsideDownBinaryTree


def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def test_upside_down_binary_tree():
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node4, node5)
    root1 = TreeNode(1, node2, node3)
    expected1 = TreeNode(4, TreeNode(5), TreeNode(2, TreeNode(3), TreeNode(1)))
    assert is_same_tree(upsideDownBinaryTree(root1), expected1)

    root2 = None
    expected2 = None
    assert is_same_tree(upsideDownBinaryTree(root2), expected2)

    root3 = TreeNode(1)
    expected3 = TreeNode(1)
    assert is_same_tree(upsideDownBinaryTree(root3), expected3)


def test_upside_down_binary_tree_large():
    root_large = TreeNode(1)
    current = root_large
    for i in range(2, 11):
        current.left = TreeNode(i)
        current = current.left

    expected_large = TreeNode(10)
    current_expected = expected_large
    for i in range(9, 0, -1):
        current_expected.right = TreeNode(i)
        current_expected = current_expected.right

    assert is_same_tree(upsideDownBinaryTree(root_large), expected_large)
