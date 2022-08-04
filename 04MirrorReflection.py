# Question: https://leetcode.com/problems/mirror-reflection/

# Solution:
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        m, n = q, p
        while m % 2 == 0 and n % 2 == 0:
            m = m // 2
            n = n // 2
        if m % 2 == 0 and n % 2 == 1: 
            return 0
        if m % 2 == 1 and n % 2 == 1: 
            return 1
        if m % 2 == 1 and n % 2 == 0:
            return 2
        return -1;
      
# Verdict:
# Runtime: 36 ms, faster than 86.14% of Python3 online submissions for Mirror Reflection.
# Memory Usage: 14 MB, less than 16.83% of Python3 online submissions for Mirror Reflection.
