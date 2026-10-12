class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            self.prefix[row][0] = matrix[row][0]
            for col in range(1, len(matrix[0])):
                self.prefix[row][col] = self.prefix[row][col-1] + matrix[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2+1):
            if col1 > 0:
                sum += self.prefix[i][col2] - self.prefix[i][col1-1]
            else:
                sum += self.prefix[i][col2]
        return sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)