# Question: https://leetcode.com/problems/minimum-number-of-refueling-stops/

# Solution:
class Solution(object):
    def minRefuelStops(self, target, fuel, s):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        heap = [] 
        s = [(0, 0)] + s + [(target, 0)]
        n, ans = len(s), 0
        
        for i in range(1, n):
            fuel -= s[i][0] - s[i-1][0]
            while heap and fuel < 0:
                fuel -= heappop(heap)
                ans += 1
            if fuel < 0: return -1
            heappush(heap, -s[i][1])
            
        return ans
      
# Verdict:
# Runtime: 166 ms, faster than 57.58% of Python online submissions for Minimum Number of Refueling Stops.
# Memory Usage: 13.6 MB, less than 81.82% of Python online submissions for Minimum Number of Refueling Stops.
