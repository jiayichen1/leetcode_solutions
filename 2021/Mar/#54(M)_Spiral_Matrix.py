class Solution:
    # Clean, naive iterative approach
    # Not the most elegant solution to check exit condition
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # DO NOT mutate these two variables; used for reference
        m, n = len(matrix[0]), len(matrix)
        # range of items to add in left/right and up/down directions
        # indices are inclusive
        left, right, up, down = 0, m-1, 0, n-1
        res = []
        
        while len(res) < m * n:
            # left to right, including right most elem
            i = left
            while i <= right and len(res) < m * n:
                res.append(matrix[up][i])
                i += 1
                
            # up to down, NOT including bottom most elem
            i = up + 1
            while i <= down-1 and len(res) < m * n:
                res.append(matrix[i][right])
                i += 1
            
            # right to left, including left most elem
            i = right
            while i >= left and len(res) < m * n:
                res.append(matrix[down][i])
                i -= 1
            
            # down to up, NOT including top most elem
            i = down - 1
            while i >= up+1 and len(res) < m * n:
                res.append(matrix[i][left])
                i -= 1
            
            left = left + 1
            right = right - 1
            up = up + 1
            down = down -1
        
        return res
                

        # crazy one-liner pythonic solution
        # return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
        