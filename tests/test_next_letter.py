from questions.next_letter import find_next_letter

from random import choice, seed
from string import ascii_lowercase
from time import time

def test_find_next_letter():
    assert find_next_letter(['a', 'c', 'f', 'h'], 'f') == 'h'
    assert find_next_letter(['a', 'c', 'f', 'h'], 'b') == 'c'
    assert find_next_letter(['a', 'c', 'f', 'h'], 'm') == 'a'
    assert find_next_letter(['a', 'c', 'f', 'h'], 'h') == 'a'
    assert find_next_letter(['a', 'b', 'c', 'd', 'e'], 'e') == 'a'


def brute_force_next_letter(letters, key):
    for letter in letters:
        if letter > key:
            return letter
    return letters[0]  

def test_efficient_find_next_letter():
    seed(42)  # to make it reproducible

    large_letters = sorted([choice(ascii_lowercase) for _ in range(10000)])
    large_key = choice(ascii_lowercase)
    
    start_time = time()
    result = find_next_letter(large_letters, large_key)
    end_time = time()
    assert (end_time - start_time) < 0.1  # should run within a fraction of a second for logN

    expected = brute_force_next_letter(large_letters, large_key)
    assert result == expected
