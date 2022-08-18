# Question: https://leetcode.com/problems/reduce-array-size-to-the-half/

# Solution:
class Solution(object):
    import heapq
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)
        heap = []
        for ob in count:
            heapq.heappush(heap, count[ob] * -1)
        
        res = ans = 0
        while heap:
            ans -= heapq.heappop(heap)
            res += 1
            if ans >= (len(arr) + 1)//2:
                return res
        
        return 0
      
# Verdict:
# Runtime: 1562 ms, faster than 6.36% of Python online submissions for Reduce Array Size to The Half.
# Memory Usage: 26.9 MB, less than 78.18% of Python online submissions for Reduce Array Size to The Half.
