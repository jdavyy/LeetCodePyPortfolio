
#diagonal matrix sum calculator

from typing import List

class Solution:
    
    def diagonalSum(self, mat: List[List[int]]) -> int:
        num = len(mat) #number of rows in the matrix
        ac = num // 2 #divides # of rows by 2

        count = 0 #count for final int return
        for x in range(num): #for each row in num rows 
            count += mat[x][x] #count adds the int at position of the number of row it is
            count += mat[num-1-x][x] #same thing but from the opposite

        if num % 2 == 1: #if the number of rows is odd
            count -= mat[ac][ac] #subtracts the value that was added twice
        return count #returns count
    

mat = [[1,2,3], [4,5,6], [7,8,9]]
solution = Solution()
print(solution.diagonalSum(mat))