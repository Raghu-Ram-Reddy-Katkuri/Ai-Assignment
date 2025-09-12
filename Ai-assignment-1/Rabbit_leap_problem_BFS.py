from collections import deque

def initial_config():
    return ('W', 'W', 'W', '_', 'E', 'E', 'E') 

def is_goal_state(configuration):
    return configuration == ('E', 'E', 'E', '_', 'W', 'W', 'W')

def generate_possible_moves(config):
    config = list(config)
    next_steps = []

    for idx in range(len(config)):
        token = config[idx]
        if token == 'W':
            if idx + 1 < len(config) and config[idx + 1] == '_':
                temp = config[:]
                temp[idx], temp[idx + 1] = temp[idx + 1], temp[idx]
                next_steps.append(tuple(temp))
            elif idx + 2 < len(config) and config[idx + 2] == '_' and config[idx + 1] in ['W', 'E']:
                temp = config[:]
                temp[idx], temp[idx + 2] = temp[idx + 2], temp[idx]
                next_steps.append(tuple(temp))

        elif token == 'E':
            if idx - 1 >= 0 and config[idx - 1] == '_':
                temp = config[:]
                temp[idx], temp[idx - 1] = temp[idx - 1], temp[idx]
                next_steps.append(tuple(temp))
            elif idx - 2 >= 0 and config[idx - 2] == '_' and config[idx - 1] in ['W', 'E']:
                temp = config[:]
                temp[idx], temp[idx - 2] = temp[idx - 2], temp[idx]
                next_steps.append(tuple(temp))

    return next_steps

def solve_with_bfs():
    queue = deque([(initial_config(), [])])
    visited = set()

    while queue:
        current, steps = queue.popleft()
        if is_goal_state(current):
            return steps + [current]
        if current in visited:
            continue
        visited.add(current)
        for neighbor in generate_possible_moves(current):
            queue.append((neighbor, steps + [current]))

    return None


solution = solve_with_bfs()

print("Sequence of Moves to Solve Rabbit Leap Puzzle:\n")
if solution:
    for index, state in enumerate(solution):
        print(f"Step {index + 1}: {state}")
else:
    print("No solution found.")