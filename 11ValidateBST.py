# Question: https://leetcode.com/problems/validate-binary-search-tree/

# Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], minn = float('-inf'), maxx = float('inf')) -> bool:
        if root is None:
            return True
        if root.val <= minn or root.val >= maxx:
            return False
        return self.isValidBST(root.left, minn, root.val) and self.isValidBST(root.right, root.val, maxx)
      
# Verdict:
# Runtime: 65 ms, faster than 61.21% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.6 MB, less than 46.02% of Python3 online submissions for Validate Binary Search Tree.
