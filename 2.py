# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Note: No need to reverse list, by default it is already reversed.
class Solution:
    def printer(self, l: ListNode):
        ss = ""
        while l is not None:
            ss += "->" + str(l.val)
            l = l.next
        print(ss)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        temp = l1
        while l1 is not None or l2 is not None:
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            if l1.next is None and l2.next is None:
                break
            elif l1.next is None:
                l1.next = ListNode(0)
            elif l2.next is None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
        if carry:
            l1.next = ListNode(carry)
        return temp
