# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. 
# Such regions are completely enclosed by 'X' cells.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
# You do not need to return anything.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:


# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]


def surrounded_region(board):
    ROW = len(board)
    COL = len(board[0])
    visited = [[False]*COL for _ in range(ROW)]
    
    def dfs(i, j):
        if i < 0 or i >= ROW or j < 0 or j >= COL or visited[i][j] or board[i][j] == "X":
            return

        visited[i][j] = True
        
        dfs(i, j+1)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i-1, j)
        
    
    #check for top and bottom
    for n in range(ROW):
        if board[n][0] == "O" and not visited[n][0]:
            dfs(n, 0)
            
        if board[n][COL-1] == "O" and not visited[n][COL-1]:
            dfs(n, COL-1)
    
    #check for left and right
    
    for m in range(COL):
        if board[0][m] == "O" and not visited[0][m]:
            dfs(0, m)
        
        if board[ROW-1][m] == "O" and not visited[ROW-1][m]:
            dfs(ROW-1, m)
    
    
    for r in range(ROW):
        for c in range(COL):
            if board[r][c] == "O" and not visited[r][c]:
                board[r][c] = "X"
    return board
                

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(surrounded_region(board))