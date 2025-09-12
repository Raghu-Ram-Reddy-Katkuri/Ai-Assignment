from collections import deque

class BridgeCrossBFS:
    def __init__(self):
        self.times = {
            'Amogh': 5,
            'Ameya': 10,
            'Grandmother': 20,
            'Grandfather': 25
        }
        self.group = set(self.times)

    def initial_state(self):
        return (frozenset(self.group), frozenset(), 'L', 0)

    def is_target_state(self, config):
        left_group, right_group, torch, elapsed = config
        return len(left_group) == 0 and elapsed <= 60

    def possible_transitions(self, config):
        left, right, torch, elapsed = config
        outcomes = []

        if torch == 'L':
            for a in left:
                for b in left:
                    if a <= b:
                        updated_left = left - {a, b}
                        updated_right = right | {a, b}
                        duration = max(self.times[a], self.times[b])
                        total_elapsed = elapsed + duration
                        if total_elapsed <= 60:
                            outcomes.append((updated_left, updated_right, 'R', total_elapsed))
        else:
            for returner in right:
                new_left = left | {returner}
                new_right = right - {returner}
                duration = self.times[returner]
                total_elapsed = elapsed + duration
                if total_elapsed <= 60:
                    outcomes.append((new_left, new_right, 'L', total_elapsed))

        return outcomes


def bfs_solver(problem_instance):
    queue = deque([(problem_instance.initial_state(), [])])
    explored = set()

    while queue:
        current_state, trail = queue.popleft()
        if problem_instance.is_target_state(current_state):
            return trail + [current_state]
        if current_state in explored:
            continue
        explored.add(current_state)

        for next_state in problem_instance.possible_transitions(current_state):
            queue.append((next_state, trail + [current_state]))

    return None


puzzle = BridgeCrossBFS()
solution_path = bfs_solver(puzzle)

print("\nBFS-Based Bridge Crossing Solution:\n")
if solution_path:
    for idx, step in enumerate(solution_path):
        left_side, right_side, torch_pos, time_used = step
        print(f"Step {idx + 1}:")
        print(f"  Left:  {set(left_side)}")
        print(f"  Right: {set(right_side)}")
        print(f"  Torch: {torch_pos}")
        print(f"  Time:  {time_used} mins\n")
else:
    print("No valid path found within the time limit.")