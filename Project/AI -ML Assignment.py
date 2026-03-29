from collections import deque

# Define the goal state as a tuple so it can't be changed and is easy to compare
GOAL = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

# Directions: (row_change, col_change) for Up, Down, Left, Right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def print_board(board, depth):
    print(f'Depth: {depth}')
    for row in board:
        print(f"{row[0]} {row[1]} {row[2]}")
    print('--------')

def solve_puzzle_bfs(start_board, start_x, start_y):
    # Convert the starting board into a tuple of tuples as tuples are immutable. 
    start_state = tuple(tuple(row) for row in start_board)
    
    # Queue stores simple tuples containing: (current_board, zero_x, zero_y, depth)
    q = deque([(start_state, start_x, start_y, 0)])
    visited = set([start_state])

    while q:
        board, x, y, depth = q.popleft()
        print_board(board, depth)

        # Check for Victory
        if board == GOAL:
            print(f'Goal state reached at depth {depth}')
            return

        # Sliding the '0' in all 4 directions
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy

            # New Position is still in the board
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                # Convert tuple back to list of lists:
                new_board = [list(r) for r in board]
                
                # Swap the '0' with the adjacent number
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]

                # Convert back to a tuple to check if the state is already visited
                new_state = tuple(tuple(r) for r in new_board)

                # If it's a new state, add it to our queue and mark it visited
                if new_state not in visited:
                    visited.add(new_state)
                    q.append((new_state, new_x, new_y, depth + 1))

    print('No solution found.')

if __name__ == '__main__':
    # Initial state
    start = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    
    print('Initial State:')
    solve_puzzle_bfs(start, 1, 1)