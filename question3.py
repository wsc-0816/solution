class Solution(object):
	def lengthOfLongest(self,s):
		'''
		type : String 
		return type: int
		This question is about getting the longest substring without repeating
		characters of the input
		'''
		if len(s) == 0:
			return 'This is an empty string'
		else:
			temp = s[0]
			re =''
			for i in s :
				if i in temp:
					if len(re) < len(temp):
						re = temp
						temp = i
					else:
						temp = i
				else:
					temp += i
			return len(re) 


if __name__ == '__main__':
	s = Solution()
	c = s.lengthOfLongest('pwwkew')
	print c



