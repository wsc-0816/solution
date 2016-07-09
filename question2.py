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
        if l1 is None or l2 is None:
            if l2 is None and l1 is None:
                return "Nothing needs to add"
            elif l1 is None:
                return l2
            else:
                return l1
        else:
            count = 0 
            lis = []
            while l1 is not None and l2 is not None:
                temp = l1.val + l2.val + count 
                if temp > 9:
                    count = 1
                    temp -= 10
                else:
                    count = 0
                lis.append(temp)
                l1 = l1.next
                l2 = l2.next
            while l1 is not None:
                temp = l1.val + count 
                if temp > 9:
                    count = 1
                    temp -= 10
                else:
                    count = 0
                lis.append(temp)
                l1 = l1.next
            while l2 is not None:
                temp = l2.val + count 
                if temp > 9:
                    count = 1
                    temp -= 10
                else:
                    count = 0
                lis.append(temp)
                l2 = l2.next
            lis.reverse()
            a = None
            for i in lis:
                LisTemp = ListNode(i)
                LisTemp.next = a 
                a = LisTemp 
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



