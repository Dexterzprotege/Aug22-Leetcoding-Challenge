# Question: https://leetcode.com/problems/power-of-four/

# Solution:
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(0, 32, 2):
            if n == 1 << i:
                return True
        return False
      
# Verdict:
# Runtime: 46 ms, faster than 8.09% of Python online submissions for Power of Four.
# Memory Usage: 13.4 MB, less than 66.91% of Python online submissions for Power of Four.
