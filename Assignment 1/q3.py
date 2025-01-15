import random
from collections import deque

class Puzzle:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.obstacles = [(0, 0), (2, 2)]
        self.robot_position = (2, 0)
        self.end_position = (0, 2)

    def move(self, direction):
        x, y = self.robot_position
        new_position = None

        if direction == "Right": 
            new_position = (x, y + 1)
        elif direction == "Up": 
            new_position = (x - 1, y)

        if new_position and self.is_valid_position(new_position):
            self.robot_position = new_position
            return True
        return False

    def is_valid_position(self, position):
        x, y = position
        return (0 <= x < self.rows and
                0 <= y < self.cols and
                position not in self.obstacles)

    def __str__(self):
        grid = [['.' for _ in range(self.cols)] for _ in range(self.rows)]
        for obstacle in self.obstacles:
            grid[obstacle[0]][obstacle[1]] = 'X'
        grid[self.robot_position[0]][self.robot_position[1]] = 'R'
        grid[self.end_position[0]][self.end_position[1]] = 'E'
        return '\n'.join([''.join(row) for row in grid])


def dfs(puzzle):
    def dfs_recursive(puzzle, path):
        if puzzle.robot_position == puzzle.end_position:
            return path

        visited.add(puzzle.robot_position)

        for move in ["Right", "Up"]:  
            new_puzzle = Puzzle()
            new_puzzle.obstacles = puzzle.obstacles.copy()
            new_puzzle.robot_position = puzzle.robot_position
            new_puzzle.end_position = puzzle.end_position
            if new_puzzle.move(move):
                if new_puzzle.robot_position not in visited:
                    result = dfs_recursive(new_puzzle, path + [move])
                    if result is not None:
                        return result

        return None

    visited = set()
    return dfs_recursive(puzzle, [])


def bfs(puzzle):
    queue = deque([(puzzle, [])])
    visited = set()

    while queue:
        current_puzzle, path = queue.popleft()

        if current_puzzle.robot_position == current_puzzle.end_position:
            return path

        if current_puzzle.robot_position not in visited:
            visited.add(current_puzzle.robot_position)

            for move in ["Up", "Right"]:  
                new_puzzle = Puzzle()
                new_puzzle.obstacles = current_puzzle.obstacles.copy()
                new_puzzle.robot_position = current_puzzle.robot_position
                new_puzzle.end_position = current_puzzle.end_position
                if new_puzzle.move(move):
                    new_path = path + [move]
                    queue.append((new_puzzle, new_path))

    return None


def dls(puzzle, depth_limit):
    def dls_recursive(current_puzzle, path, depth):
        if current_puzzle.robot_position == current_puzzle.end_position:
            return path

        if depth == 0:
            return None

        for move in ["Right", "Up"]:  
            new_puzzle = Puzzle()
            new_puzzle.obstacles = current_puzzle.obstacles.copy()
            new_puzzle.robot_position = current_puzzle.robot_position
            new_puzzle.end_position = current_puzzle.end_position
            if new_puzzle.move(move):
                result = dls_recursive(new_puzzle, path + [move], depth - 1)
                if result is not None:
                    return result

        return None

    return dls_recursive(puzzle, [], depth_limit)


def ids(puzzle, max_depth):
    for depth in range(max_depth + 1):
        result = dls(puzzle, depth)
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    puzzle = Puzzle()
    
    dfs_solution = dfs(puzzle)
    print("DFS Solution:", dfs_solution)
    
    bfs_solution = bfs(puzzle)
    print("BFS Solution:", bfs_solution)
    
    depth_limit = 10 
    dls_solution = dls(puzzle, depth_limit)
    print(f"DLS Solution (depth limit {depth_limit}):", dls_solution)
    
    max_depth = 20
    ids_solution = ids(puzzle, max_depth)
    print("IDS Solution:", ids_solution)
