# Question: https://leetcode.com/problems/power-of-three/

# Solution:
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n == 3 ** (round(math.log(n) / math.log(3)));
      
# Verdict:
# Runtime: 120 ms, faster than 57.76% of Python online submissions for Power of Three.
# Memory Usage: 13.7 MB, less than 14.97% of Python online submissions for Power of Three.
