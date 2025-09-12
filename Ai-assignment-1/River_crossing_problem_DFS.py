class BridgePuzzle:
    def __init__(self):
        self.travel_time = {
            'Amogh': 5,
            'Ameya': 10,
            'Grandmother': 20,
            'Grandfather': 25
        }
        self.people = set(self.travel_time.keys())

    def get_initial_state(self):
        return (frozenset(self.people), frozenset(), 'L', 0)

    def is_goal_state(self, state):
        left_side, right_side, lamp_position, elapsed_time = state
        return len(left_side) == 0 and elapsed_time <= 60

    def generate_moves(self, state):
        left_side, right_side, lamp_position, current_time = state
        next_states = []

        if lamp_position == 'L':
            for person1 in left_side:
                for person2 in left_side:
                    if person1 <= person2:
                        new_left = left_side - {person1, person2}
                        new_right = right_side | {person1, person2}
                        move_time = max(self.travel_time[person1], self.travel_time[person2])
                        total_time = current_time + move_time
                        if total_time <= 60:
                            next_states.append((new_left, new_right, 'R', total_time))
        else:
            for returnee in right_side:
                updated_left = left_side | {returnee}
                updated_right = right_side - {returnee}
                move_back_time = self.travel_time[returnee]
                total_time = current_time + move_back_time
                if total_time <= 60:
                    next_states.append((updated_left, updated_right, 'L', total_time))

        return next_states


def depth_first_search(puzzle_obj):
    frontier = [(puzzle_obj.get_initial_state(), [])]
    visited = set()

    while frontier:
        current_state, journey = frontier.pop()
        if puzzle_obj.is_goal_state(current_state):
            return journey + [current_state]
        if current_state in visited:
            continue
        visited.add(current_state)

        for new_state in puzzle_obj.generate_moves(current_state):
            frontier.append((new_state, journey + [current_state]))

    return None


puzzle_instance = BridgePuzzle()
solution = depth_first_search(puzzle_instance)

print("DFS Solution for Bridge Problem:\n")
if solution:
    for step_index, step in enumerate(solution):
        left_side, right_side, lamp, elapsed = step
        print(f"Step {step_index + 1}:")
        print(f"   Left Side:  {set(left_side)}")
        print(f"   Right Side: {set(right_side)}")
        print(f"   Lamp Side:  {lamp}")
        print(f"   Time Taken: {elapsed} minutes\n")
else:
    print("No feasible path found within 60 minutes.")