def calculate_perimeter_area(grid):
    rows = len(grid)
    cols = len(grid[0])
    total_area = rows*cols
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Directions for vertical and horizontal neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    # Flood fill using DFS to identify and calculate area and perimeter
    def dfs(x, y, char):
        stack = [(x, y)]
        visited[x][y] = True
        area = 0
        perimeter = 0
        touching_same_type = 0
        
        while stack:
            cx, cy = stack.pop()
            area += 1
            cell_perimeter = 4

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny):
                    if grid[nx][ny] == char:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                            cell_perimeter -= 2
                        touching_same_type += 1
            if (in_bounds(cx + 1, cy) and in_bounds(cx, cy + 1) and in_bounds(cx + 1, cy + 1) and grid[cx][cy] == grid[cx + 1][cy] == grid[cx][cy + 1] == grid[cx + 1][cy + 1]):
                cell_perimeter -= 2  # Subtract 2 from perimeter for the 2x2 cube
            perimeter += cell_perimeter

        return area, perimeter




    total_cost = 0
    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                char = grid[i][j]
                area, perimeter = dfs(i, j, char)
                total_cost += area * perimeter
                print(f"Region of {char} - Area: {area}, Perimeter: {perimeter}, Cost: {area * perimeter}")
    return total_cost




def read_grid_from_file(file_path):
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    return grid

# Read the grid
file_path = 'grid.txt'
grid = read_grid_from_file(file_path)

# Calculate total cost
total_cost = calculate_perimeter_area(grid)
print(f"Total cost of fences: {total_cost}")