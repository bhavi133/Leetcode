Link : https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Code :

import collections

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        n = head
        while n is not None:
            l.append(n.val)
            n = n.next
        
        dic = collections.Counter(l)
        k = []
        for i, j in dic.items():
            if j == 1:
                k.append(i)
        
        if len(k) != 0:
            head_node = ListNode(k[0])
            new_node = head_node
            for i in range(1, len(k)):
                new_node.next = ListNode(k[i])
                new_node = new_node.next
            return head_node
        else:
            return  
