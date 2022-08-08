# Question: https://leetcode.com/problems/longest-increasing-subsequence/

# Solution:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        return max(dp)
      
# Verdict:
# Runtime: 7783 ms, faster than 5.71% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.2 MB, less than 47.45% of Python3 online submissions for Longest Increasing Subsequence.
