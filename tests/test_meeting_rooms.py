from questions.meeting_rooms import minMeetingRooms
def test_min_meeting_rooms():
    assert minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    assert minMeetingRooms([[7,10],[2,4]]) == 1
    
    assert minMeetingRooms([[0, 10**6]] * 10**4) == 10**4
    assert minMeetingRooms([[i, i+1] for i in range(10**4)]) == 1

    assert minMeetingRooms([[7, 10]]) == 1

    assert minMeetingRooms([[5, 10], [10, 15], [15, 20]]) == 1

    assert minMeetingRooms([[5, 10], [7, 11], [8, 12]]) == 3

    assert minMeetingRooms([[7, 10], [5, 8]]) == 2
