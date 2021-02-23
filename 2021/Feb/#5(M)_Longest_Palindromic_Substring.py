class Solution:
    # METHOD 1
    # copied from leetcode China
    # slower and uses more space than METHOD 2
    # expand function continues expanding outward until invalid,
    # then return the boundaries
    # main function iterates through possible centers and use
    # the expand function to see how far it gets
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]
    
    # METHOD 2
    # grows outward; treat center 'frame' (same char string) as one
    def findLongest(self, s, lowB, range_):
            # find the furtherest end of this 'frame'
            highB = lowB
            
            while highB < len(s) - 1 and s[lowB] == s[highB + 1]:
                highB += 1
            
            # at this point, the substring from lowB to highB is a 
            # string with the same char;
            # record the highB index for returning later
            ans = highB

            # grow lowB and highB outward until not palindrome
            while lowB > 0 and highB < len(s) - 1 and s[lowB - 1] == s[highB + 1]:
                lowB -= 1
                highB += 1

            # if our new found indices are better, put them back to range_
            if highB - lowB > range_[1] - range_[0]:
                range_[0] = lowB
                range_[1] = highB
            
            # return highB as the next starting point
            return ans
        
    def longestPalindrome2(self, s: str) -> str:
        # base cases
        if s == None or len(s) == 0:
            return ""

        range_ = [0, 0]
        i = 0
        while i < len(s):
            i = self.findLongest(s, i, range_)
            # i was where the last center 'frame' ended
            # adding 1 attempts to start looking for the next center 'frame'
            i += 1
        
        return s[range_[0]:range_[1]+1]
    