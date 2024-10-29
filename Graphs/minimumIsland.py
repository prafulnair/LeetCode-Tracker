
def explore(grid, r, c, seen):
    rinBounds = (0 <= r and r <= len(grid)-1)
    cinBounds = (0 <= c and c <= len(grid[0])-1)

    if (not rinBounds or not cinBounds):
        return 0
    if (r,c) in seen:
        return 0
    if grid[r][c] == 'W':
        return 0
    
    seen.add((r,c))
    size = 1

    size += explore(grid, r-1, c, seen)
    size += explore(grid, r+1, c, seen)
    size += explore(grid, r, c-1, seen)
    size += explore(grid, r, c+1, seen)
    #print(size)
    return size


def findMinIsland(grid):
    seen = set()
    minSize = float("inf")

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = explore(grid, r, c, seen)
            if size > 0:
                minSize = min(minSize, size)

    return minSize



island_grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(findMinIsland(island_grid))


