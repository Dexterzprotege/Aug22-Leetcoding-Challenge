# Question: https://leetcode.com/problems/unique-paths/

# Solution:
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
      
# Verdict:
# Runtime: 44 ms, faster than 65.78% of Python3 online submissions for Unique Paths.
# Memory Usage: 13.9 MB, less than 32.97% of Python3 online submissions for Unique Paths.
