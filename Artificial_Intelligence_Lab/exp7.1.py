def dfs(maze, start, end):
    stack = [start]  # Stack for DFS
    visited = set()  # Set of visited cells
    came_from = {}   # Dictionary to reconstruct path

    while stack:
        position = stack.pop()
        x, y = position

        if position == end:
            # Reconstruct path
            path = []
            while position != start:
                path.append(position)
                position = came_from[position]
            path.append(start)
            path.reverse()
            return True, path

        if position in visited:
            continue

        visited.add(position)

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            next_pos = (new_x, new_y)

            if (0 <= new_x < len(maze) and
                0 <= new_y < len(maze[0]) and
                maze[new_x][new_y] == 0 and
                next_pos not in visited):

                stack.append(next_pos)
                came_from[next_pos] = position  # Track the path

    return False, []  # No path found

# Example maze: 0 = open, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

# Run DFS and get the path
path_exists, path = dfs(maze, start, end)

if path_exists:
    print("true")
    print("Path:", path)
else:
    print("No path exists.")
