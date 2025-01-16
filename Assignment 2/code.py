import math
from queue import PriorityQueue

class Node:
    def __init__(self, position, is_obstacle=False):
        self.position = position
        self.is_obstacle = is_obstacle
        self.g = float('inf')  
        self.h = 0 
        self.f = float('inf')  
        self.parent = None
    
    def __lt__(self, other):
        return self.f < other.f

class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.nodes = [[Node((x, y)) for y in range(height)] for x in range(width)]
        for x, y in obstacles:
            self.nodes[x][y].is_obstacle = True
    
    def get_neighbors(self, node, search_type='a_star'):
        x, y = node.position
        neighbors = []
        if search_type == 'a_star':
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
        else:
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.nodes[nx][ny].is_obstacle:
                neighbors.append(self.nodes[nx][ny])
        return neighbors

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def calculate_heuristics(grid, end):
    for x in range(grid.width):
        for y in range(grid.height):
            grid.nodes[x][y].h = euclidean_distance((x, y), end)

def greedy_search(grid, start, end):
    start_node = grid.nodes[start[0]][start[1]]
    end_node = grid.nodes[end[0]][end[1]]
    open_list = PriorityQueue()
    open_list.put((start_node.h, id(start_node), start_node))
    closed_set = set()
    
    while not open_list.empty():
        current_node = open_list.get()[2]
        if current_node == end_node:
            return reconstruct_path(current_node)
        closed_set.add(current_node)
        for neighbor in grid.get_neighbors(current_node, search_type='greedy'):
            if neighbor in closed_set:
                continue
            if neighbor not in [n for _, _, n in open_list.queue]:
                neighbor.parent = current_node
                open_list.put((neighbor.h, id(neighbor), neighbor))
    return None 

def a_star(grid, start, end):
    start_node = grid.nodes[start[0]][start[1]]
    end_node = grid.nodes[end[0]][end[1]]
    start_node.g = 0
    start_node.f = start_node.h
    open_list = PriorityQueue()
    open_list.put((start_node.f, id(start_node), start_node))
    closed_set = set()
    
    while not open_list.empty():
        current_node = open_list.get()[2]
        if current_node == end_node:
            return reconstruct_path(current_node)
        closed_set.add(current_node)
        for neighbor in grid.get_neighbors(current_node, search_type='a_star'):
            if neighbor in closed_set:
                continue
            tentative_g = current_node.g + 1  
            if tentative_g < neighbor.g:
                neighbor.parent = current_node
                neighbor.g = tentative_g
                neighbor.f = neighbor.g + neighbor.h
                if neighbor not in [n for _, _, n in open_list.queue]:
                    open_list.put((neighbor.f, id(neighbor), neighbor))
    return None  

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  

def print_grid(grid, path, start, end):
    for y in range(grid.height):
        for x in range(grid.width):
            if (x, y) == start:
                print("S", end=" ")
            elif (x, y) == end:
                print("E", end=" ")
            elif grid.nodes[x][y].is_obstacle:
                print("X", end=" ")
            elif (x, y) in path:
                print("O", end=" ")
            else:
                print(".", end=" ")
        print()

width, height = 3, 3
obstacles = [(0, 0), (2, 2)]
start = (0, 2)  
end = (2, 0)   
grid = Grid(width, height, obstacles)
calculate_heuristics(grid, end)

print("Heuristic values:")
for y in range(height):
    for x in range(width):
        node = grid.nodes[x][y]
        print(f"{node.h:.2f}" if not node.is_obstacle else "  X  ", end=" ")
    print()

# Greedy Search
greedy_path = greedy_search(grid, start, end)
print("\nGreedy Search:")
if greedy_path:
    print("Path found:", " -> ".join(str(pos) for pos in greedy_path))
    print("\nGrid with Greedy Search path:")
    print_grid(grid, greedy_path, start, end)
else:
    print("No path found.")

# A* Search
a_star_path = a_star(grid, start, end)
print("\nA* Search:")
if a_star_path:
    print("Path found:", " -> ".join(str(pos) for pos in a_star_path))
    print("\nGrid with A* Search path:")
    print_grid(grid, a_star_path, start, end)
else:
    print("No path found.")

# Cost comparison
print("\nComparison:")
print(f"Greedy Search path length: {len(greedy_path) - 1 if greedy_path else 'N/A'}")
print(f"A* Search path length: {len(a_star_path) - 1 if a_star_path else 'N/A'}")
