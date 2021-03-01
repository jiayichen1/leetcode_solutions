class Solution:
    def nextPermutation(self, nums: List[int]) -> None
        # The general idea is to find the split point of prefix and suffix, called the pivot
        # The suffix is non-increasing (which means this portion is the highest permutation)
        # Swap the pivot with with the smallest value in suffix that's larger than pivot.
        # Lastly, sort the suffix portion by reversering all elements.
        # More rationale behind it: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm 
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        # loop to find the 'pivot': the beginning of a 
        # non-increasing suffix
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # already is the last permutation
        if i <= 0:
            nums.reverse()
            return
        
        j = len(nums) - 1
        i = i - 1   # pivot index
        # loop to find the smallest value in the suffix 
        # to swap with the 'pivot'
        while nums[j] <= nums[i]:
            j -= 1
        
        # swap pivot and the swapee in the suffix
        nums[i], nums[j] = nums[j], nums[i]
        
        # sort the 'sufix' by reversing it
        nums[i+1:] = nums[len(nums)-1 : i : -1]
        
        return
        