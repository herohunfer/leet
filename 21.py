# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        current = result
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l2 is None else l2
        return result.next

# # recursively    
# def mergeTwoLists2(self, l1, l2):
#     if not l1 or not l2:
#         return l1 or l2
#     if l1.val < l2.val:
#         l1.next = self.mergeTwoLists(l1.next, l2)
#         return l1
#     else:
#         l2.next = self.mergeTwoLists(l1, l2.next)
#         return l2