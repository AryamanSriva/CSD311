import random

class Puzzle:
    def __init__(self):
        self.grid_size = (3, 3)
        self.obstacle_coords = [(0, 0), (2, 2)]
        self.robot_start = (2, 0)
        self.goal = (0, 2)
        self.robot_position = self.robot_start

    def attempt_move(self, direction):
        current_x, current_y = self.robot_position

        if direction == 0:
            return None
        elif direction == 1:
            return None
        elif direction == 2:
            new_position = (current_x, current_y + 1)
        elif direction == 3:
            new_position = (current_x - 1, current_y)
        else:
            return None

        if self.is_valid(new_position):
            self.robot_position = new_position
            return True
        return False

    def is_valid(self, position):
        x, y = position
        rows, cols = self.grid_size
        return (0 <= x < rows and 0 <= y < cols and position not in self.obstacle_coords)

    def simulate_moves(self, move_limit):
        move_count = 0
        for _ in range(move_limit):
            possible_moves = [2, 3]
            chosen_move = random.choice(possible_moves)

            if not self.attempt_move(chosen_move):
                print(f"Move {move_count + 1}: Invalid move. Simulation stopped.")
                break

            move_count += 1
            move_name = 'Right' if chosen_move == 2 else 'Up'
            print(f"Move {move_count}: {move_name}")

            if self.robot_position == self.goal:
                print("Robot has reached the goal!")
                break
        return move_count

    def display_grid(self):
        rows, cols = self.grid_size
        grid_representation = [['.' for _ in range(cols)] for _ in range(rows)]

        for obstacle in self.obstacle_coords:
            grid_representation[obstacle[0]][obstacle[1]] = 'X'

        robot_x, robot_y = self.robot_position
        goal_x, goal_y = self.goal

        grid_representation[robot_x][robot_y] = 'R'
        grid_representation[goal_x][goal_y] = 'E'

        return '\n'.join([''.join(row) for row in grid_representation])

def main():
    game = Puzzle()

    print("Initial grid layout:")
    print(game.display_grid())

    moves = int(input("\nEnter the number of moves: "))
    print("\nSimulating moves:")
    total_moves = game.simulate_moves(moves)

    print(f"\nGrid layout after {total_moves} moves:")
    print(game.display_grid())

if __name__ == "__main__":
    main()
