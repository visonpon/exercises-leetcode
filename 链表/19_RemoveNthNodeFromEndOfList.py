class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        l=r=dummy
        for i in range(n+1):
            r=r.next
        while r:
            l=l.next
            r=r.next
        l.next=l.next.next
        return dummy.next
        
'''
https://www.cnblogs.com/grandyang/p/4606920.html
'''
class solution(obejct):
    def removeNthFromEnd(head,n):
        if(!head.next):
            return NULL
        pre = cur = head
        for i in range(n):
            cur = cur.next
        if(!cur):
            return head.next
         while(cur.next):
             cur = cur.next
             pre = pre.mext
             
         pre.next = pre.next.next
         return head
         
