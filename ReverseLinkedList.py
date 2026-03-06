# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head
        prev = head
        head = head.next
        nextNode = head.next
        head.next = prev
        prev.next = None
        while nextNode != None:
            prev = head
            head = nextNode
            nextNode = head.next
            head.next = prev
        return head


