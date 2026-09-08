# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = list1
        curr_l2 = list2

        start = ListNode()
        newList = start

        while curr_l1 is not None and curr_l2 is not None:
            if curr_l1.val >= curr_l2.val:
                newList.next = curr_l2
                curr_l2 = curr_l2.next
            else:
                newList.next = curr_l1
                curr_l1 = curr_l1.next

            newList = newList.next

        if curr_l1 is not None:
            newList.next = curr_l1
        else:
            newList.next = curr_l2

        return start.next

                
                
