"""
"""

def explore(grid, r, c, seen):
    
    rowInbounds = (0 <= r and r < len(grid))
    colInbounds = (0 <= c and c < len(grid[0]))

    # Check if we are not going out of bounds with row and columnds
    if(not rowInbounds or not colInbounds):
       return False
    
    if (grid[r][c]) == 'W':
        return False

    if (r,c) in seen:
        return False
    
    # cycle avoiding logic
    seen.add((r,c))

    explore(grid, r-1, c, seen) # explore up
    explore(grid, r+1, c, seen) # explore down
    explore(grid, r, c-1, seen) # explore left
    explore(grid, r, c+1, seen) # explore right

    return True #i have finished exploring a new island (neighbours of the node)





def countIsland(grid):
    count = 0 # for island counting
    seen  = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if explore(grid, i, j, seen) == True:
                count += 1

    return (count)

 


island_grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(countIsland(island_grid))









  