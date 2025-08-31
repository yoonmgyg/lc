class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head
        while current and current.next:
            after = current.next

            # swap first and second nodes
            prev.next = after
            current.next = after.next
            after.next = current
            # move nodes forward
            prev = current
            current = current.next

        return dummy.next
