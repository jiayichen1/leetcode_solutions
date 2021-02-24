class Solution:
    # METHOD 1: from lc discussion board
    # essentially searching in a very efficient way
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1  # init result to the first int
        k -= 1  # minus one to account for our initial guess
        
        while k > 0:
            interval = [result, result+1]   # for counting number of integers prefixed with result
            steps = 0   # steps inbetween some interval
            
            while interval[0] <= n:
                steps += (min(interval[1], n+1) - interval[0])  # plus one is needed for counting the correct steps
                interval = [interval[0]*10, interval[1]*10]
            
            # if steps are not enough to get to k, skip to next digit
            if k >= steps:
                k -= steps
                result += 1
            # otherwise, do a round of FINER search
            else:
                k -= 1
                result *= 10
            
        return result


    # METHOD 2: naive sorting solution
    # DID NOT PASS TIME LIMIT TEST
    def findKthNumber2(self, n: int, k: int) -> int:
        def lex_compare(item1, item2):
            item1, item2 = str(item1), str(item2)
            # ndigits1, ndigits2 = int(math.log10(item1)) + 1, int(math.log10(item2)) + 1
            
            for i in range(min(len(item1), len(item2))):
                if item1[i] == item2[i]:
                    continue
                elif item1[i] < item2[i]:
                    return -1
                else:
                    return 1
            
            if len(item1) < len(item2):
                return -1
            elif len(item1) > len(item2):
                return 1
            else:
                return 0
        
        digits = list(range(1, n+1))
        
        digits = sorted(digits, key=cmp_to_key(lex_compare))
        
        return digits[k-1]
        