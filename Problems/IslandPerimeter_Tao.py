class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        elif len(grid) == 1:
            if len(grid[0]) == 1:
                return 4 * grid[0][0]
            else:
                res = 0
                for j in range(len(grid[0])):
                    if grid[0][j] == 1:
                        if j == 0:
                            res += 4 - grid[0][1]
                        elif j == len(grid[0]) - 1:
                            res += 4 - grid[0][j - 1]
                        else:
                            res += 4 - grid[0][j - 1] - grid[0][j + 1]
                return res

        else:
            if len(grid[0]) == 0:
                return 0
            elif len(grid[0]) == 1:
                res = 0
                for i in range(len(grid)):
                    if grid[i][0] == 1:
                        if i == 0:
                            res += 4 - grid[1][0]
                        elif i == len(grid) - 1:
                            res += 4 - grid[i - 1][0]
                        else:
                            res += 4 - grid[i + 1][0] - grid[i - 1][0]
                return res
            else:
                res = 0
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 1:
                            if i == 0 and j == 0:
                                res += (4 - grid[1][0] - grid[0][1])
                            elif i == len(grid) - 1 and j == 0:
                                res += (4 - grid[i - 1][j] - grid[i][j + 1])
                            elif i == 0 and j == len(grid[0]) - 1:
                                res += (4 - grid[i + 1][j] - grid[i][j - 1])
                            elif i == len(grid) - 1 and j == len(grid[0]) - 1:
                                res += (4 - grid[i - 1][j] - grid[i][j - 1])
                            elif i == 0:
                                res += (4 - grid[i + 1][j] - grid[i][j + 1] - grid[i][j - 1])
                            elif j == 0:
                                res += (4 - grid[i + 1][j] - grid[i - 1][j] - grid[i][j + 1])
                            elif i == len(grid) - 1:
                                res += (4 - grid[i - 1][j] - grid[i][j + 1] - grid[i][j - 1])
                            elif j == len(grid[0]) - 1:
                                res += (4 - grid[i + 1][j] - grid[i - 1][j] - grid[i][j - 1])
                            else:
                                res += (4 - grid[i + 1][j] - grid[i - 1][j] - grid[i][j + 1] - grid[i][j - 1])
                return res
