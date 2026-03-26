# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
from collections import deque

def orangesRotting(grid):
    q = deque()
    time, fresh = 0, 0
    ROWS = len(grid)
    COLS = len(grid[0])
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            
            if grid[r][c] == 2:
                q.append([r, c])
    
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc+c
                if(row < 0 or row == len(grid) or col < 0 or col == len(grid[0])
                   or grid[row][col] != 1):
                    continue
                
                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1
        
        time += 1
    return time if fresh == 0 else -1
        
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))




# q = deque()
#     time, fresh = 0, 0
    
#     ROWS, COLS = len(grid), len(grid[0])
    
#     for r in range(ROWS):
#         for c in range(COLS):
#             if grid[r][c] == 1:
#                 fresh += 1
            
#             if grid[r][c] == 2:
#                 q.append([r, c])
    
#     directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#     while q and fresh > 0:
#         #this loop will go to all the rotten oranges and the adjacent aswell
#         for i in range(len(q)):
#             #we pop the coordinates of the rotten orange 
#             r, c = q.popleft()
#             #loop over the 4 directions we can move in
#             for dr, dc in directions:
#                 #this is to get the fresh adjacent oranges to the rotten ones
#                 row, col = dr + r, dc + c
#                 # if outbounds and not fresh continue
#                 if(row < 0 or row == len(grid) or col < 0 or col == len(grid[0])
#                    or grid[row][col] != 1):
#                     continue
                
#                 # if in bounds and fresh, make rotten
#                 grid[row][col] = 2
#                 q.append([row, col])
#                 fresh -= 1
#         time += 1
    
#     return time if fresh == 0 else -1