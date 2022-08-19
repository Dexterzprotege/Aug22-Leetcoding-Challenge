# Question: https://leetcode.com/problems/split-array-into-consecutive-subsequences/

# Solution:
class Solution(object):
    def isPossible(self, A):
        left = collections.Counter(A)
        end = collections.Counter()
        for i in A:
            if not left[i]: continue
            left[i] -= 1
            if end[i - 1] > 0:
                end[i - 1] -= 1
                end[i] += 1
            elif left[i + 1] and left[i + 2]:
                left[i + 1] -= 1
                left[i + 2] -= 1
                end[i + 2] += 1
            else:
                return False
        return True
      
# Verdict:
# Runtime: 1124 ms, faster than 19.23% of Python online submissions for Split Array into Consecutive Subsequences.
# Memory Usage: 14.8 MB, less than 48.08% of Python online submissions for Split Array into Consecutive Subsequences.
