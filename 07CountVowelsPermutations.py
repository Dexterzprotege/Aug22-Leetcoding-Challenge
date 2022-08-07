# Question: https://leetcode.com/problems/count-vowels-permutation/

# Solution:
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if not n :
            return 0
        a, e, i, o, u = 1, 1, 1, 1, 1
        for x in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        return (a + e + i + o + u) % (10**9+7)
      
# Verdict:
# Runtime: 273 ms, faster than 80.85% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 14.2 MB, less than 68.69% of Python3 online submissions for Count Vowels Permutation.
