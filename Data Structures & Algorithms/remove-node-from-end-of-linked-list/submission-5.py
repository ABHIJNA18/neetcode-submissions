# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)

        l,r=dummy,head

        while n>0:
            r=r.next
            n-=1
        
        #now l is at dummy which points to beginning
        # right is at a gap of 2 which is n from left ( left is actually 3 steps away because it points to dummy )
        #once l and r are in position, just shift them by 1 until r is none

        while r:
            r=r.next
            l=l.next
        l.next=l.next.next
        return dummy.next

        