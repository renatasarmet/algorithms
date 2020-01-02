# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ok = False
        result = []
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
            
        while not ok:
            if l1.val <= l2.val:
                result.append(ListNode(l1.val))
                
                if(len(result) > 1):
                    result[-2].next = result[-1]
                    
                if l1.next == None: #acabou a l1
                    result.append(ListNode(l2.val))
                    result[-2].next = result[-1]
                    while l2.next != None: # finaliza a l2
                        l2 = l2.next
                        result.append(ListNode(l2.val))
                        result[-2].next = result[-1]
                    ok = True
                else:
                    l1 = l1.next
            else:
                result.append(ListNode(l2.val))
                
                if(len(result) > 1):
                    result[-2].next = result[-1]
                    
                if l2.next == None: #acabou a l2
                    result.append(ListNode(l1.val))
                    result[-2].next = result[-1]
                    while l1.next != None: # finaliza a l1
                        l1 = l1.next
                        result.append(ListNode(l1.val))
                        result[-2].next = result[-1]
                    ok = True
                else:
                    l2 = l2.next
            
        return result[0]
        