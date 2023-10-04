from questions.glass_towers import glass_tower

def test_glass_tower():
    assert abs(glass_tower(1, 1, 1) - 0.00000) < 1e-5
    assert abs(glass_tower(2, 1, 1) - 0.50000) < 1e-5
    assert abs(glass_tower(100000009, 33, 17) - 1.00000) < 1e-5
    assert abs(glass_tower(3, 2, 0) - 0) < 1e-5
    assert abs(glass_tower(3, 2, 1) - 0) < 1e-5
    assert abs(glass_tower(100, 9, 2) - 1.0000) < 1e-5
    assert abs(glass_tower(8, 3, 0) - 0.12500) < 1e-5
    assert abs(glass_tower(8, 3, 1) - 0.87500) < 1e-5
    assert abs(glass_tower(8, 3, 2) - 0.87500) < 1e-5
    assert abs(glass_tower(8, 3, 3) - 0.12500) < 1e-5