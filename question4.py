class Solution(object):
	def findMedian(self,l1,l2):
		i = 0 
		median = 0
		while i < len(l1) and i < len(l2):
			num1 = l1[i]
			num2 = l2[i]
			if num1 < num2:
				temp1 = l2[:i]
				temp2 = l2[i:]
				temp1.append(num1)
				l2 = temp1 + temp2
			else:
				i += 1
		length = len(l2)
		if length % 2 == 0:
			print "sdc"
			median = (l2[length/2] + l2[length/2 - 1])/2
		else:
			median = l2[length/2 + 1]
		return median 

if __name__ == '__main__':
	s = Solution()
	l1 = [1,3]
	l2 = [2,4]
	c = s.findMedian(l1,l2)
	print c



 
