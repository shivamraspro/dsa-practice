class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix) + 1, len(matrix[0]) + 1
        self.sums = [[0]*cols for _ in range(rows)]

        for i in range(1, rows):
            pre_row_sum = 0
            for j in range(1, cols):
                pre_row_sum += matrix[i-1][j-1]
                above = self.sums[i-1][j]
                self.sums[i][j] = pre_row_sum + above
        
        # for i in range(rows):
        #     for j in range(cols):
        #         print(self.sums[i][j], end="  ")
        #     print()

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        topleft = self.sums[row1][col1]
        topright = self.sums[row1][col2+1]
        bottomleft = self.sums[row2+1][col1]
        bottomright = self.sums[row2+1][col2+1]
        return bottomright - topright - bottomleft + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)