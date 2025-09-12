from collections import deque

class RabbitGame:
    def get_start(self):
        return ('W', 'W', 'W', '_', 'E', 'E', 'E')

    def is_finished(self, state):
        return state == ('E', 'E', 'E', '_', 'W', 'W', 'W')

    def possible_moves(self, state):
        state = list(state)
        moves = []

        for i in range(len(state)):
            if state[i] == 'W':
                if i + 1 < len(state) and state[i + 1] == '_':
                    new_state = state[:]
                    new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                    moves.append(tuple(new_state))
                elif i + 2 < len(state) and state[i + 2] == '_' and state[i + 1] in ['W', 'E']:
                    new_state = state[:]
                    new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                    moves.append(tuple(new_state))

            elif state[i] == 'E':
                # Move E to the left
                if i - 1 >= 0 and state[i - 1] == '_':
                    new_state = state[:]
                    new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                    moves.append(tuple(new_state))
                elif i - 2 >= 0 and state[i - 2] == '_' and state[i - 1] in ['W', 'E']:
                    new_state = state[:]
                    new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                    moves.append(tuple(new_state))

        return moves


def solve_with_dfs(game):
    stack = [(game.get_start(), [])]
    seen = set()

    while stack:
        current, path = stack.pop()
        if game.is_finished(current):
            return path + [current]
        if current in seen:
            continue
        seen.add(current)
        for move in game.possible_moves(current):
            stack.append((move, path + [current]))

    return None


game = RabbitGame()
solution = solve_with_dfs(game)

print("Path to Goal:\n")
if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")