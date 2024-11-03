class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        affected = set()
        def makeRowZero(matrix,row):
            for i in range(0, len(matrix[0])):
                if (row,i) not in affected and matrix[row][i]!=0:
                    affected.add((row,i))
                    matrix[row][i] = 0

        def makeColZero(matrix, col):
            for i in range(0, len(matrix)):
                if (i, col) not in affected and matrix[i][col]!=0:
                    affected.add((i,col))
                    matrix[i][col] = 0

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0 and (i,j) not in affected:
                    makeRowZero(matrix, i)
                    makeColZero(matrix, j)

