# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre=None
        cur=head
        while cur: 
            nxt=cur.next#注意这个技巧，我们在循环内部定义nxt而不是外面。这样防止当head=None的情况。
            cur.next=pre
            pre=cur
            cur=nxt
        return pre
   
 #头结点倒插，类似于思路一,原链表头结点依次插入新链表的开头，返回新链表  
 class Solution(object):
    def reverseList(self, head):
        newhead=None
        while head:
            p=head
            head=head.next
            p.next=newhead
            newhead=p
        return newhead

        
 '''
 https://blog.csdn.net/chinwuforwork/article/details/51399360 --- 递归
 '''       
class Solution(object):
    def reverseList(self, head):
        return self.doReverse(head, None)
    def doReverse(self, head, newHead):
        if head is None:
            return newHead
        next = head.next
        head.next = newHead
        return self.doReverse(next, head)
