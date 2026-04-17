# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. 
# One cell is a square with side length 1. The grid is rectangular, width and
# height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:


# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# Example 2:

# Input: grid = [[1]]
# Output: 4
# Example 3:

# Input: grid = [[1,0]]
# Output: 4
import collections

def island_perimeter(grid):
    
    ROW = len(grid)
    COL = len(grid[0])
    
    visited = set()
    
    def dfs(r, c):
        if r >= ROW or c >= COL or grid[r][c] == 0 or r < 0 or c < 0:
            return 1
        
        if(r, c) in visited:
            return 0
        visited.add((r, c))
        
        perimeter = dfs(r, c+1)
        perimeter += dfs(r+1, c)
        perimeter +=dfs(r, c-1)
        perimeter += dfs(r-1, c)
        return perimeter
            
    for i in range(ROW):
        for j in range(COL):
            if grid[i][j] == 1:
                return dfs(i, j)

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(island_perimeter(grid))
        
