# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

 
# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1


# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

import collections

def number_of_islands(grid):
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    island = 0
    
    def bfs(i, j):
        q=collections.deque()
        q.append((i, j))
        visited.add((i, j))
        
        while q:
            r, c = q.popleft()
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            for dr, dc in directions:
                row, col = dr+r, dc+c
                if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row, col) not in visited):
                    visited.add((row, col))
                    q.append((row, col))
            
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and (i, j) not in visited:
                bfs(i, j)
                island += 1
    return island  

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(number_of_islands(grid))
    
    
    