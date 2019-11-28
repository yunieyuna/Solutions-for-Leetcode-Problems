# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 原地址：https://blog.csdn.net/liuxiao214/article/details/77937839
        # 思路一：利用stack。将两个链表分别压入栈。然后同时出栈，找到第一个不相等节点即可返回。如果栈顶就不相同，则直接返回空。

        # 思路二：同时遍历两个链表。遍历条件是两个节点不相等。如果在遍历过程中，有节点走到了结尾，就从头再重新走，这样，在你追我赶中，两个节点会因为相等，或者同为空，发生碰头。

        # 思路三：这里难点无非是两个链表长度不相等。跟思路二相同，不同的是，有节点到了结尾后，从头走的不是当前链表的头了，而是另一个链表的头。比如，L1的长度是5，L2的长度是6，当p1走到L1的结尾，p2才走到L2的第6个，此时，L1剩余长度0，L2剩余长度1。这样，p1马上走到L2的头，则L1剩余长度为6，L2走完最后一个节点后，再去走L1，其剩余长度也变成1+5=6，此时两个链表长度相等了，则找到相同节点指日可待。而且比思路二中快很多。
        
        # 思路3代码
        if headA == None or headB == None:
            return None
        
        # 2 pointers
        pa = headA
        pb = headB
        
        while pa != pb:
            if pa != None:
                pa = pa.next
            else:
                pa = headB
            if pb != None:
                pb = pb.next
            else:
                pb = headA
        return pa
