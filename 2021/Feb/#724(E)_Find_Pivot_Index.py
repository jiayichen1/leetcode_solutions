class Solution:
	# find the total sum
	# keep track of the accumulative sum as we go over the list
	# if the sum so far is half of (total sum - curr element)
	# then we FOUND the pivot Index
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_so_far = 0
        for i in range(len(nums)):
            if sum_nums == sum_so_far * 2 + nums[i]:
                return i
            sum_so_far += nums[i]
        
        return -1
        