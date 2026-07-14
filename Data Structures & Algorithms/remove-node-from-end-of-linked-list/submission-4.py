# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        length=1
        while cur.next:
            length+=1
            cur=cur.next
        print(length)

        if length==1:
            head=None
            return head
        
        k=length-n+1
        print(k)
        #special case
        if k==1:
            head=head.next
            return head
        #now delete node at kth place

        count=1
        l,r=head,head

        while r:
            if count==k:
                l.next=r.next
                r=r.next
                break
            else:
                count+=1
                l=r
                r=r.next
        return head
                




        
        