class Solution(object):
    def islandPerimeter(self, grid):
        self.t = grid
        l = len(grid)  # Length
        result = 0
        for i in range(len(grid)):  # Number of rows
            for j in range(len(grid[0])):  # Number of columns
                if grid[i][j] == 1:
                    ct = 4
                    ct -= self.checkNeighbor(i - 1, j)
                    ct -= self.checkNeighbor(i + 1, j)
                    ct -= self.checkNeighbor(i, j - 1)
                    ct -= self.checkNeighbor(i, j + 1)
                    result += ct
        return result

    def checkNeighbor(self, i, j):
        if i >= 0 and i < len(self.t) and j >= 0 and j < len(self.t[0]):
            if self.t[i][j] == 1:
                return 1
        return 0