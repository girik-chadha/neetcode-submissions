# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1=[]
        curr = head
        #now we have a the order of the linked list in the list
        while curr:
            l1.append(curr)
            curr=curr.next
        L,R = 0, len(l1)-1
        curr=head
        curr.next=l1[R]
        curr=curr.next
        L+=1
        R-=1
        if len(l1)%2==0:
            while L<R:
                curr.next=l1[L]
                curr=curr.next
                curr.next=l1[R]
                curr=curr.next
                L+=1
                R-=1
        else: 
             while L<=R:
                if L==R:
                    curr.next=l1[R]
                    curr=curr.next
                    break
                curr.next=l1[L]
                curr=curr.next
                curr.next=l1[R]
                curr=curr.next
                L+=1
                R-=1
        curr.next=None
                
                
                


        
