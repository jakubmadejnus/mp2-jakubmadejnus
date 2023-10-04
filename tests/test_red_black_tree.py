from questions.red_black_tree import RBTree, RBNode

def test_RBTree():
    rbtree = RBTree()

    # Basic Insertion
    rbtree.insert(30)
    assert rbtree.get_sorted_keys() == [30]

    rbtree.insert(20)
    assert rbtree.get_sorted_keys() == [20, 30]

    rbtree.insert(10)
    assert rbtree.get_sorted_keys() == [10, 20, 30]

    # Complex Insertions
    items = [20, 15, 25, 10, 5, 1, 30, 35, 40]
    for item in items:
        rbtree.insert(item)
        assert rbtree.get_sorted_keys() == sorted(items[:items.index(item)+1])

    # Further testing a potential left rotation
    rbtree = RBTree()
    rbtree.insert(30)
    rbtree.insert(40)
    rbtree.insert(50)
    assert rbtree.get_sorted_keys() == [30, 40, 50]

    # Further testing a potential right rotation
    rbtree = RBTree()
    rbtree.insert(30)
    rbtree.insert(20)
    rbtree.insert(10)
    assert rbtree.get_sorted_keys() == [10, 20, 30]

    # Larger Test Case
    rbtree = RBTree()
    items = list(range(100, 0, -1))
    for item in items:
        rbtree.insert(item)
        assert rbtree.get_sorted_keys() == sorted(items[:items.index(item)+1])
