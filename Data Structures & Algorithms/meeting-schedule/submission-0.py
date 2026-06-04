"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ivals = []
        for ival in intervals:
            ivals.append((ival.start, ival.end))

        ivals.sort()
        print(ivals)

        for i in range(1, len(ivals), 1):
            if ivals[i-1][1] > ivals[i][0]:
                return False

        return True
