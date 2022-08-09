# Question: https://leetcode.com/problems/binary-trees-with-factors/

# Solution:
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr = sorted(arr)
        dic = defaultdict(int)
        
        for a in arr:
            temp = 1
            for b in arr:
                if b > a:
                    break
                else:
                    temp += (dic[b] * dic[a/b])
            dic[a] = temp
        
        return sum(dic.values())%(10**9+7)
      
# Verdict:
# Runtime: 2146 ms, faster than 11.61% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 70.4 MB, less than 5.05% of Python3 online submissions for Binary Trees With Factors.
