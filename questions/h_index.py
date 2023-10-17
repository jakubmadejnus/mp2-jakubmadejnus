"""
Problem: H-Index Calculation

Description:
Given an array of integers `citations` where each entry `citations[i]` represents the number of citations a researcher received for their ith paper, determine the researcher's h-index.

According to the definition of h-index: An h-index is the largest value `h` such that there are at least `h` papers having `h` or more citations.

Function Signature:
def h_index(citations: List[int]) -> int:

Inputs:
    - citations (List[int]): A list of integers where each entry denotes the number of citations for the respective paper.

Returns:
    - int: The h-index value for the researcher based on the provided citations.

Examples:
1. Input: [3,0,6,1,5]
   Output: 3
   Explanation: The researcher has 5 papers with the citations [3,0,6,1,5]. 
                Three of the papers have at least 3 citations, and the rest have fewer than 3 citations, thus the h-index is 3.

2. Input: [1,3,1]
   Output: 1
   Explanation: The researcher has 3 papers with the citations [1,3,1]. 
                Only one paper has at least 1 citation and the rest have 1 or fewer citations, thus the h-index is 1.

Notes:
    - A variation of counting sort or a priority queue can be employed to find the h-index efficiently in n log n time.
    - Sorting the citations in descending order can help determine the h-index by comparing the citation value with its index.

Tags:
    - Sorting
    - Priority Queue
    - Arrays
    - Amazon Interview Question
"""

from typing import List

def h_index(citations: List[int]) -> int:

    if len(citations) == 0:
        return 0

    # sort
    citations.sort()
    citations.reverse()

    for i in range(len(citations)):
        if i+1 >= citations[i]:
            return citations[i]
    return(len(citations))