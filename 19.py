# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node1 = head
        node2 = head
        for _ in range(n):
            node2 = node2.next
        if node2 == None:
            return head.next
        while node2.next != None:
            node1 = node1.next
            node2 = node2.next
        node1.next = node1.next.next
        return head

# Index and Remove - AC in 56 ms

# In this solution I recursively determine the indexes again, but this time my helper function removes the nth node. It returns two values. The index, as in my first solution, and the possibly changed head of the remaining list.

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def remove(head):
#             if not head:
#                 return 0, head
#             i, head.next = remove(head.next)
#             return i+1, (head, head.next)[i+1 == n]
#         return remove(head)[1]