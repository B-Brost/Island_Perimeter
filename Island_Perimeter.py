def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # go through each cell, multiply each cell by 4
    # for each cell with value greater than 0, subtract 1 from each of the cells adjacent to it.
    # if value greater than 0 add it to perimeter_value
    perimeter=0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] >0:
                perimeter+=4
                try:
                    if grid[i][j+1] >0 and j != len(grid[0]):
                        perimeter-=1
                except IndexError:
                    pass
                try:
                    if grid[i+1][j] >0 and i !=len(grid):
                        perimeter-=1
                except IndexError:
                    pass
                try:
                    if grid[i][j-1] >0 and j!=0:
                        perimeter-=1
                except IndexError:
                    pass
                try:
                    if grid[i-1][j] >0 and i!=0:
                        perimeter-=1
                except IndexError:
                    pass
    return perimeter
        
grid = [[1]]
print(islandPerimeter(grid))
