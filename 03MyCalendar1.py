# Question: https://leetcode.com/problems/my-calendar-i/

# Solution:
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if start < e and end > s:
                return False
        self.calendar.append((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end) 

# Verdict:
# Runtime: 554 ms, faster than 38.82% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.7 MB, less than 92.29% of Python3 online submissions for My Calendar I.
