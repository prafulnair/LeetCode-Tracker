class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        
        if m * n != len(original):
            return []

        res = []
        k = 0
        for i in range(0, m):
            row = []
            for j in range(0, n):
                row.append(original[k])
                k += 1
            res.append(row)

        return res