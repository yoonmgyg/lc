class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_head = dummy
        while list1 and list2: # add lower linked list to next
            if (list1.val < list2.val):
                new_head.next = list1
                list1 = list1.next
            else:
                new_head.next = list2
                list2 = list2.next
            new_head = new_head.next

        if list1: # add remaining linked list to the end
            new_head.next = list1
        
        elif list2:
            new_head.next = list2

        return dummy.next
