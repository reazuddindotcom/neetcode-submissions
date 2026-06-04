"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        timestamps = []
        for ival in intervals:
            timestamps.append((ival.start, 1)) # 1 for start time
            timestamps.append((ival.end, 0))   # 0 for start time

        timestamps.sort()
        # print(timestamps)
        
        rooms = 0
        active = 0
        for t in timestamps:
            if t[1] == 1:
                active += 1
                rooms = max(rooms, active)
            else:
                active -= 1

        return rooms