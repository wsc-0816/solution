class Solution(object):
	def threeSum(self,nums):
		if (len(nums) <= 2):
			return "This list is too short"
		result = []
		i = 0
		nums_length = [(i + 1) for i in range(len(nums) - 1)]
		print nums_length
		i = 0
		while i < len(nums) -2:
			temp = 0 - nums[i]
			j = 0
			x = 1
			while j < len(nums_length)-1:
				if nums[nums_length[j]]+ nums[nums_length[x]] == temp:
					temp_one = sorted([nums[i],nums[nums_length[j]],nums[nums_length[x]]])
					if temp_one not in result:
						result.append(temp_one)
					x += 1
				if x == len(nums_length)-1:
					j += 1
					x = j+1
				else:
					x += 1	
			i += 1
			del nums_length[0] 
		return result
if __name__ == '__main__':
	test = Solution()
	a = test.threeSum([1,-1,0])
	print a 

