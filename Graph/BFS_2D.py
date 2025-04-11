from collections import deque

# Direction Vectors
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

# Function to check if a cell is visited or not
def isValid(vis, row, col):
    if (row < 0 or col < 0 or row >= 4 or col >= 4):  # If cell lies out of bounds
        return False
    
    if (vis[row][col]):  # If cell is already visited
        return False
    
    return True

def BFS(grid, vis, row, col):
    q = deque()  # Creating a queue to process nodes in BFS
    q.append((row, col))  # Appending first node in queue
    vis[row][col] = True  # Mark true for visited node

    # Iterate while queue is not empty
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        print(grid[x][y], end = " ")

        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy)):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True

if __name__ == "__main__":
    grid =  [ [ 1, 2, 3, 4 ],
           [ 5, 6, 7, 8 ],
           [ 9, 10, 11, 12 ],
           [ 13, 14, 15, 16 ] ]
    
    vis = [[False for i in range(4)] for i in range(4)]

    BFS(grid, vis, 0, 0)

# Time Complexity: O(N * M)
# Auxiliary Space: O(N * M)




