class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional
    [ListNode]:
        dummy = ListNode(-1)
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

#         self.next = next
#         self.val = val
#     def __init__(self, val=0, next=None):
# class ListNode:
# Definition for singly-linked list.
