class Solution:
    # METHOD 1
    # linear scanning
    # lcp will become shorter in the loop; if some word doesn't 
    # share the lcp at all, break from the loop and return empty str
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for s in strs[1:]:
            prefix = self.lcp(prefix, s)
            
            if not prefix:
                break
            
        return prefix
    
    def lcp(self, str1, str2):
        minLength, index = min(len(str1), len(str2)), 0
        
        while index < minLength and str1[index] == str2[index]:
            index += 1
        
        return str1[:index]
        