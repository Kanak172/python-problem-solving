class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:

            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            digit = total % 10
            carry = total // 10

            new_node = ListNode(digit)
            current.next = new_node
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next