"""
Problem: Minimum Conference Rooms Required

Description:
Given an array of meeting time intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required to accommodate all the meetings without any overlap.

Function Signature:
def minMeetingRooms(intervals: List[List[int]]) -> int:

Inputs:
    - intervals (List[List[int]]): A list of lists where each inner list represents a meeting's start and end times.

Returns:
    - int: The minimum number of conference rooms required.

Examples:
1. Input: [[0,30],[5,10],[15,20]]
   Output: 2
   Explanation: We can schedule the meetings [0,30] and [15,20] in one room and [5,10] in another room.

2. Input: [[7,10],[2,4]]
   Output: 1
   Explanation: The meetings can be scheduled in the same room without overlap.

Notes:
    - A priority queue can be used to keep track of the end times of meetings. For each new meeting, if its start time is after the earliest end time, then it can be accommodated in the same room.
    - The size of the priority queue will give us the number of rooms required.

Tags:
    - Priority Queue
    - Sorting
    - Arrays
    - TikTok Interview Question
"""

from typing import List
import heapq

def minMeetingRooms(intervals: List[List[int]]) -> int:

    if not intervals:
        return 0

    # Initialize a heap.
    free_rooms = []

    # sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    # For all the remaining meeting rooms
    for i in intervals:
        
        # If the current meeting's start time is greater than or equal to the earliest end time in the heap
        if free_rooms and free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)
            
        # Add the current meeting's ending time to the heap.
        heapq.heappush(free_rooms, i[1])
    
    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)