# Question: https://leetcode.com/problems/combination-sum-iv/

# Solution:
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for total in range(1, target + 1):
            dp[total] = 0
            for n in nums:
                if total-n >= 0 and total-n <= target:
                    dp[total] += dp[total-n]
        return dp[-1]
      
# Verdict:
# Runtime: 57 ms, faster than 64.59% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 13.8 MB, less than 98.86% of Python3 online submissions for Combination Sum IV.
