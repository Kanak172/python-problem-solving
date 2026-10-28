# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head

        last = head
        totalNodes = 1

        while last.next:
            totalNodes += 1
            last = last.next

        k %= totalNodes
        if k == 0:
            return head

        totalNodesMinusK = totalNodes - k 
        curr = head
        
        while totalNodesMinusK >1:
            curr = curr.next
            totalNodesMinusK -= 1

        newHead = curr.next
        curr.next = None
        last.next = head

        return newHead

        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        