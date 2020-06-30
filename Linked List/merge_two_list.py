# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        if l1.val < l2.val:
            new = ListNode(val = l1.val, next = l1.next)
            l1 = l1.next
        else:
            new = ListNode(val = l2.val, next = l2.next)
            l2 = l2.next
        new = new.next
        while n1.next != None and n2.next != None:
            if n1.next.val < n2.next.val:
                new.next.val = n1.next.val
                new.next.next = n1.next.next
                n1 = l1.next
                new = new.next
            else:
                new.next.val = n2.next.val
                new.next.next = n2.next.next
                n2 = l2.next
                new = new.next
        if n1.next != None:
            new.next = n1.next
        if n2.next != None:
            new.next = n2.next
        return new

X = Solution
print(X.mergeTwoLists(X, [1,2,4], [1,3,4]))