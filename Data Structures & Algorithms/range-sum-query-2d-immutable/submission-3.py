class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.mat = [[0]*c for _ in range(r)]

        for i in range(r):
            sum = 0
            for j in range(c):
                sum += matrix[i][j]
                self.mat[i][j] = sum
        
        # for i in range(r):
        #     for j in range(c):
        #         print(f"{self.mat[i][j]}  ", end="")
        #     print()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        if col1 == 0:
            for i in range(row1, row2+1):
                sum += self.mat[i][col2]
        else:
            for i in range(row1, row2+1):
                sum += self.mat[i][col2] - self.mat[i][col1-1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)