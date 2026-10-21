class Solution:
    def merge2Lists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2              # attach the leftover part
        return dummy.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        if len(lists) % 2 == 0:           # make length odd
            lists.append(None)
        mid = len(lists) // 2

        for i in range(1, mid + 1):
            lists[i] = self.merge2Lists(lists[i], lists[i - 1])          # left sweep  →
            lists[-i - 1] = self.merge2Lists(lists[-i - 1], lists[-i])   # right sweep ←

        return lists[mid]