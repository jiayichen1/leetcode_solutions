class Solution:
	# METHOD 1: go over sorted intervals in order
	# if curr int's beginning is larger than res's latest interval ending, then update
 	# otherwise, update res's latest interval ending
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sorted_int = sorted(intervals, key=lambda x: x[0])
        
        for interval in sorted_int:
        	# not res is a special case for the very first interval (when res is empty)
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        
        return res

    # METHOD 2: user two pointers to dynamically look for split points
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        sorted_int = sorted(intervals, key=lambda x: x[0])
        i = 0
        
        while i < len(sorted_int):
            currBound = sorted_int[i][1]
            j = i + 1
            
            while j < len(sorted_int) and sorted_int[j][0] <= currBound:
                currBound = max(currBound, sorted_int[j][1])
                j += 1
                
            res.append([sorted_int[i][0], currBound])
            i = j
        
        return res
        