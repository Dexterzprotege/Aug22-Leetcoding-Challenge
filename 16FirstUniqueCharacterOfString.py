# Question: https://leetcode.com/problems/first-unique-character-in-a-string/

# Solution:
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = [0] * 26
        for c in s:
            dic[ord(c)-ord('a')] += 1
            
        for i in range(len(s)):
            c = s[i]
            if dic[ord(c)-ord('a')] == 1:
                return i
        return -1
            
# Verdict:
# Runtime: 128 ms, faster than 83.69% of Python online submissions for First Unique Character in a String.
# Memory Usage: 14.6 MB, less than 10.98% of Python online submissions for First Unique Character in a String.
