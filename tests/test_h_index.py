from questions.h_index import h_index

def test_h_index():
    assert h_index([3,0,6,1,5]) == 3
    assert h_index([1,3,1]) == 1
    
    assert h_index([1000]*1000 + [0]*1000) == 1000
    
    assert h_index([i for i in range(10**5, 0, -1)]) == 50000

    assert h_index([1] * 10**5) == 1

    assert h_index([i for i in range(1, 10**5 + 1)]) == 10**5 // 2

    assert h_index([]) == 0
    
    assert h_index([0, 0, 0]) == 0
    
    assert h_index([5, 5, 5, 5]) == 4
    
    assert h_index([10, 9, 8, 7, 6]) == 5
