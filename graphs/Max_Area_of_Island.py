# You are given an m x n binary matrix grid. An island is a group 
# of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:

# Input: grid = [
#     [0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
#     [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
#     [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
#     ]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
import collections

def max_area_of_islan(grid):
    if not grid:
        return 0
    
    visited = set()
    
    ROW = len(grid)
    COL = len(grid[0])
    
    def bfs(r, c):
        q =  collections.deque()
        q.append((r, c))
        visited.add((r, c))
        
        island = 1
        while q:
            row, col = q.popleft()
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                
                if nr in range(ROW) and nc in range(COL) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    island += 1
                    q.append((nr, nc))
                    visited.add((nr, nc))
        return island
    
    max_island = 0
    
    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1 and (r, c) not in visited:
                max_island = max(max_island, bfs(r, c))
    return max_island

grid = [
[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
]

print(max_area_of_islan(grid))
