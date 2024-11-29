# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li=[]
        for i in range(0,len(lists)):
            temp=lists[i]
            while(temp!=None):
                li.append(temp.val)
                temp=temp.next
        li.sort()
        head=ListNode(None)
        for i in li:
            nn=ListNode(i)
            if head==None:
                head=nn
                continue
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=nn
        print(li)
        return head.next