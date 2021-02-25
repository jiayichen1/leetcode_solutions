class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        # advance the left ptr
        for left in range(len(nums)-2):
            # a really SUBTLE point to avoid duplicates:
            # basically if the left ptr realizes that the value
            # it points to is the same as the previous one
            # Then it should skip it because otherwise it would
            # cause duplicate triplets by checking a subset of 
            # what has already been checked
            if left > 0 and nums[left] == nums[left-1]:
                continue
            
            mid, right = left+1, len(nums)-1
            
            while mid < right:
                s = nums[left] + nums[mid] + nums[right]
                
                if s < 0:
                    mid += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append((nums[left], nums[mid], nums[right]))
                    # skip dup numbers by advancing mid ptr
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    mid, right = mid+1, right-1
        
        return res