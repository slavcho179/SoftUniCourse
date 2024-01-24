# Read User input
n = int(input())

matrix = [[int(x) for x in input().split()] for i in range(n)]
coordinates = ((int(x) for x in c.split(",")) for c in input().split())

# Initialise directions
directions = (
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1),  # top left
    (-1, 1),   # top right
    (1, -1),   # bottom left
    (1, 1),     # bottom right
    (0, 0),  # current -> important
)

# Logic
for row, col in coordinates:
    if matrix[row][col] < 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

active_cells = [num for row in range(n) for num in matrix[row] if num > 0]

# Print User output
print(f"Alive cells: {len(active_cells)}")
print(f"Sum: {sum(active_cells)}")

[print(*row) for row in matrix]