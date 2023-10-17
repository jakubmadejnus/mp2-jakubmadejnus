"""
Problem: Glass Towers

Description:
Given a champagne tower with glasses stacked in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on up to the 100th row. 
Each glass can hold exactly one cup of champagne. When champagne is poured onto the topmost glass, if it overflows, the excess champagne is equally distributed to the glasses immediately to its left and right. If a glass on the bottom row overflows, the excess champagne is lost.

Determine the volume of champagne in a particular glass after pouring a certain number of cups into the top of the tower.

Function Signature:
def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:

Inputs:
    - poured (int): The total number of cups of champagne poured onto the top glass.
    - query_row (int): The 0-indexed row number of the queried glass.
    - query_glass (int): The 0-indexed position of the queried glass in its row.

Returns:
    - float: The volume of champagne in the queried glass after pouring the specified amount. Return the result rounded to 5 decimal places.

Examples:

1. Input: poured = 1, query_row = 1, query_glass = 1
   Output: 0.00000

2. Input: poured = 2, query_row = 1, query_glass = 1
   Output: 0.50000

3. Input: poured = 100000009, query_row = 33, query_glass = 17
   Output: 1.00000

Notes:
    - Consider the propagation of overflow in a cascading manner from the top glass to the bottom glasses.
    - The result should be constrained between 0 and 1, as glasses can't hold more than 1 cup or less than 0 cups.

Tags:
    - Simulation
    - Binary Trees
    - TikTok Interview Question
"""

def glass_tower(poured: int, query_row: int, query_glass: int) -> float:

    glasses = [[0] * k for k in range(1, 102)]

    glasses[0][0] = poured

    for row in range(100):  # Up to the 100th row
        for col in range(row + 1):  # Each glass in the row
            overflow = max(0, glasses[row][col] - 1)  # Calculate the overflow
            if overflow > 0:
                # Distribute the overflow equally to the glasses diagonally below
                glasses[row + 1][col] += overflow / 2
                glasses[row + 1][col + 1] += overflow / 2
                # Adjust the current glass's volume
                glasses[row][col] = 1  # Current glass is full

    volume = min(1, max(0, glasses[query_row][query_glass]))
    return round(volume, 5)
