class Solution:
    '''
    There are simpler solutions w/o sliding window.
    Links to some discussions:
    [Java] https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/discuss/96693/Java-4-lines-concise-solution-with-explanation
    [Python] https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/discuss/96712/Simple-Python
    '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pt1, pt2, result = 0, 0, 0
        while pt2 < len(nums):
            while pt2 < len(nums) and nums[pt2] == 1:
                pt2 += 1
            result = max(result, pt2-pt1)
            while pt2 < len(nums) and nums[pt2] == 0:
                pt2 += 1
                pt1 = pt2
        return result
        