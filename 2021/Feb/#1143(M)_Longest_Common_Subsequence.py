class Solution:
    # METHOD 1: basic dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i+1][j+1] = dp[i][j] + 1 if c == d else max(dp[i+1][j], dp[i][j+1])
        
        return dp[m][n]

    # METHOD 2: space optimized dp
    # 10% space improv but 50% time drop
    # key is to switch rows for updates 
    # and figure out where the last values are
    # Refer to the discussion board if necessary:
    # https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # use the shorter string as the basis for dp
        # swap the string order to save some extra space
        if m < n:
            return self.longestCommonSubsequence(text2, text1)
    
        # 2 rows, n columns dp aka space optimized
        dp = [[0]*(n+1) for _ in range(2)]
        
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[1 - i % 2][j+1] = dp[i % 2][j] + 1 if c == d else max(dp[1 - i % 2][j], dp[i % 2][j+1])
        
        return dp[m % 2][n]
