# Question: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# Code:
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left, right, n = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def lessK(m):
            count = 0
            for r in range(n):
                x = bisect_right(matrix[r], m)
                count += x
            return count
        
        while left < right:
            mid = (left + right) // 2
            if lessK(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left
      
# Verdict:
# Runtime: 297 ms, faster than 54.96% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 18.7 MB, less than 80.82% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
