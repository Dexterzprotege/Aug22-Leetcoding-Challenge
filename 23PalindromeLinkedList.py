# Question: https://leetcode.com/problems/palindrome-linked-list/

# Solution:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev
        
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        first = reverse(slow)
        second = head
        
        while first:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        
        return True
      
# Verdict:
# Runtime: 1419 ms, faster than 65.35% of Python online submissions for Palindrome Linked List.
# Memory Usage: 67.4 MB, less than 75.54% of Python online submissions for Palindrome Linked List.
