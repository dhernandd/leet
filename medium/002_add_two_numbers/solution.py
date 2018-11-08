# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# My solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        l1_val = 0 if l1 is None else l1.val
        l2_val = 0 if l2 is None else l2.val
        val = l1_val + l2_val + carry
        carry, val = val//10, val%10
        l = head = ListNode(val)
        
        while True:
            l1 = l1.next if l1 is not None else l1
            l2 = l2.next if l2 is not None else l2
            
            if l1 is None and l2 is None:
                if carry:
                    l.next = ListNode(carry)
                break

            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val
            val = l1_val + l2_val + carry
            carry, val = val//10, val%10
            
            l.next = ListNode(val)
            l = l.next

        return head



# Much more elegant, think of this as accumulating on carry
class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev = result = ListNode(None)
        
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            prev.next = ListNode(carry%10)
            prev = prev.next
            carry //= 10
            
        return result.next
