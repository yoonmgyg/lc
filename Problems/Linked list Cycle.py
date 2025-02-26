# Use fast pointer and check if slow and fast match
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False
