class Solution(object):
	def threeSum(self,nums):
		if (len(nums) <= 2):
			return "This list is too short"
		result = []
		i = 0
		while i < len(nums) - 2:
			temp = 0 - nums[i] - nums[i+1]
			j= i + 2
			while j < len(nums):
				if nums[j] == temp:
					result.append([nums[i],nums[i+1],nums[j]])
				j += 1
			i += 1 
		return result
if __name__ == '__main__':
	test = Solution()
	a = test.threeSum([1,-1,0,-1,2,-4])
	print a 