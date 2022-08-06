# Question: https://leetcode.com/problems/poor-pigs/

# Solution:
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
        
# Verdict:
# Runtime: 51 ms, faster than 38.69% of Python3 online submissions for Poor Pigs.
# Memory Usage: 14 MB, less than 20.44% of Python3 online submissions for Poor Pigs.
