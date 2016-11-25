class Solution(object):
    def islandPerimeter(self, grid):
        self.grid = grid
        l = len(grid)  # Length
        result = 0
        for i in range(len(grid)):  # Number of rows
            for j in range(len(grid[0])):  # Number of columns
                if grid[i][j] == 1:
                    ct = 4
                    ct -= self.checkNeighbor(i - 1, j)
                    ct -= self.checkNeighbor(i + 1, j)
                    ct -= self.checkNeighbor(i, j - 1)
                    ct -= self.heckNeighbor(i, j + 1)
                    result += ct
        return result


    def checkNeighbor(self, i, j):
        if i >= 0 and i < len(self.grid) and j >= 0 and j < len(self.grid[0]):
            if self.grid[i][j] == 1:
                return 1
        return 0


    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]

    print(len(grid))

    print(islandPerimeter(grid))
