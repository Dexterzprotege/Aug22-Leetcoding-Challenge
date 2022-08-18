# Question: https://leetcode.com/problems/unique-morse-code-words/

# Solution:
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        
        s = set()
        for word in words:
            x = ""
            for c in word:
                x += MORSE[ord(c)-ord('a')]
            s.add(x)
            
        return len(s)
      
# Verdict:
# Runtime: 37 ms, faster than 40.47% of Python online submissions for Unique Morse Code Words.
# Memory Usage: 13.5 MB, less than 43.14% of Python online submissions for Unique Morse Code Words.
