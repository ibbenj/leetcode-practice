# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get size of list
        size = 0
        curNode = head
        while curNode != None:
            size += 1
            curNode = curNode.next

        if size-n == 0:
            return head.next
        else:
            prevNode = None
            curNode = head
            for _ in range(size-n):
                prevNode = curNode
                curNode = curNode.next

            prevNode.next = curNode.next

        return head
    
"""
Time: O(n)

First iteration to get size of linked list.
Second iteration to remove element
"""
        