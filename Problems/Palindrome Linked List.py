class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next: # get middle of list
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow: # reverse second half of list
            next_ = slow.next
            slow.next = prev
            prev = slow
            slow = next_

        start = head
        while (start and prev): # check that first ahlf and second half are matching
            if (start.val != prev.val):
                return False
            start = start.next
            prev = prev.next
        
        return True
