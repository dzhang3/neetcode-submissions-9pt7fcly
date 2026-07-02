"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:[x.start,x.end])
        end = 0
        for i in intervals:
            if end > i.start:
                return False
            end = max(end,i.end)
        return True