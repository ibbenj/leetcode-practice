# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumList = None
        root = sumList

        carry = False

        while l1 is not None or l2 is not None:
            sum = carry
            if l1 is not None:
                sum += l1.val
            
            if l2 is not None:
                sum += l2.val

            if sum >= 10:
                sum -= 10
                carry = True
            else:
                carry = False

            newNode = ListNode(sum, None)
            if root is None:
                root = newNode
                sumList = newNode
            else:
                sumList.next = newNode
                sumList = sumList.next

            # Next entry
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2


        if carry is True:
            newNode = ListNode(1, None)
            sumList.next = newNode
            sumList = sumList.next 

        return root
        