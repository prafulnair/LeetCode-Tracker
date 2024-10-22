class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        if not mat or not mat[0]: return []

        rows, cols = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1

        for _ in range(rows * cols):
            result.append(mat[row][col])

            if direction == 1:  # Moving up-right
                if col == cols - 1:  # Hit the right boundary
                    row += 1
                    direction = -1
                elif row == 0:  # Hit the top boundary
                    col += 1
                    direction = -1
                else:  # Move up-right normally
                    row -= 1
                    col += 1
            else:  # Moving down-left
                if row == rows - 1:  # Hit the bottom boundary
                    col += 1
                    direction = 1
                elif col == 0:  # Hit the left boundary
                    row += 1
                    direction = 1
                else:  # Move down-left normally
                    row += 1
                    col -= 1

        return result

