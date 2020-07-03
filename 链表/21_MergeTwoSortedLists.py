class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h=l=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                l.next=l1
                l=l.next
                l1=l1.next
            else:
                l.next=l2
                l=l.next
                l2=l2.next
        while l1:
            l.next=l1
            l=l.next
            l1=l1.next
        while l2:
            l.next=l2
            l=l.next
            l2=l2.next
        return h.next
	
'''
[blog](https://www.cnblogs.com/lightwindy/p/8503688.html)
'''
class solution:
    def mergeTwoLists(head1,head2):
        temp = None
	if head1 == None:
	    return head2
	if head2 == None:
	    return head1
	if head1.val < head2.val:
	    temp = head1
	    temp.next = mergeTwoLists(head1.next,head2)
	else:
	    temp = head2
	    temp.next = mergeTwoLists(head1,head2.next)
	return temp
	    
	    
		
空间复杂度是O1，而不是On，这比一次次新建节点实例要强多了。
