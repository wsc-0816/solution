# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None :
        	if l2 is None:
        		return "Nothing needs to add"
        	else:
        		return l2
        else:
        	a= ListNode(None)
        	count = 0
        	while (l1 is not None and l2 is not None ):
        		addSum = l1.val + l2.val + count 
        		print addSum
        		if addSum >= 10:
        			 count = 1 
        			 addSum -= 10
        		else:
        			count = 0
        		for 
        		a.val = addSum
        		temp = ListNode(None)
        		a.next = temp 
        		l1= l1.next
        		l2= l2.next
        	while (l1 is not None):
        		if (count == 0 ):
        			a.next = l1
        		else:
        			while l1.val is 9:
	        			a.next.val = 0
	        			l1 = l1.next
	        		a.next.val = l1.next.val + 1
	        		a.next.next = l1.next.next
	        while (l2 is not None):
	        	if (count == 0 ):
        			a.next = l2.next
        		else:
        			while l2.next.val is 9:
	        			a.next.val = 0
	        			l2 = l2.next
	        		a.next.val = l2.next.val + 1
	        		a.next.next = l2.next.next
	        return a











if __name__ == '__main__':
	l1 = ListNode(2)
	l1.next = ListNode(3)
	l1.next.next = ListNode(4)
	l2 = ListNode(2)
	l2.next = ListNode(3)
	l2.next.next = ListNode(4)
	s = Solution()
	c = s.addTwoNumbers(l1,l2)
	while c is not None:
		print "The Value is %s" %c.val
		c= c.next



