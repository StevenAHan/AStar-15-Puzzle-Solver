'''
Project 1:
A* Algorithm for the 15-Puzzle Problem
Steven Han and Preston Tang
CS 4613
'''

# from asyncore import write
import heapq

goal = [[0] * 4 for i in range(4)]
weight = 0.0

# Our nodes, containing the state of the board, the current path cost, and a pointer to the parent
class Node:
    def __init__(self, curr_state, parent, cost, prev_action, depth):
        self.curr_state = curr_state
        self.parent = parent
        self.cost = cost
        self.prev_action = prev_action
        self.depth = depth

    def __lt__(self, other):
        return self.cost < other.cost


# The algorithm used to solve the puzzle
# returns a tuple: (total nodes generated, goal node)
def a_star_algorithm(start):
    # Each node should have a tuple of its f(n), and its resulting board state
    frontier = []
    # key is the state, and the value is the lowest path cost
    reached = dict()
    nodes_generated = 1
    initial_node = Node(start, None, initialize_start_cost(start), None, 0)
    heapq.heappush(frontier, (initial_node.cost, initial_node))
    while len(frontier):
        # Each node should have a priority value calculated from our weighted A*, and the resulting board state
        node = frontier.pop()[1]
        if (node.depth > 500): # Temporarily added this due to infinite node bug
            break
        if node.curr_state == goal:
            return (nodes_generated, node)
        for node in expand_node(node):
            # update nodes generated
            if str(node.curr_state) not in reached or node.cost < reached[str(node.curr_state)]:
                nodes_generated += 1
                reached[str(node.curr_state)] = node.cost
                heapq.heappush(frontier, (node.cost, node))

            # This part is for debugging
            print(node.prev_action, node.depth, int(node.cost))
            print('\n'.join(['  '.join([str(cell) for cell in row]) for row in node.curr_state]))
            print()
    # If no solution
    return "FAILURE"

# Finds the total cost of the current matrix
# Does manhattan distance on all nodes that aren't matched up with goal
# Adds path cost, then multiplied by weight
def find_weighted_cost(curr_node, change):
    prev_node = curr_node.parent
    # look in the goal state, and see where the change value should be, and how far away the current change is from it
    total_cost = 0
    # find the value in the goal
    for r1 in range(len(goal)):
        for c1 in range(len(goal[r1])):
            if curr_node.curr_state[change[0]][change[1]] == goal[r1][c1]:
                # Does manhattan distance
                total_cost += (abs(change[0] - r1) + abs(change[1] - c1))
    # f(n) = h(n) * W + g(n)
    total_cost *= weight
    total_cost += prev_node.cost
    return total_cost

def initialize_start_cost(curr_matrix):
    # look in the goal state, and see where the change value should be, and how far away the current change is from it
    total_cost = 0
    for r in range(len(curr_matrix)):
        for c in range(len(curr_matrix[r])):
            # If they don't match up, calculate manhattan distance
            if curr_matrix[r][c] != goal[r][c]:
                # Find where it is in goal
                # Guaranteed to find node
                for r1 in range(len(goal)):
                    for c1 in range(len(goal[r1])):
                        if curr_matrix[r][c] == goal[r1][c1]:
                            # Does manhattan distance
                            total_cost += (abs(r - r1) + abs(c - c1))
    # f(n) = h(n) * W + g(n)
    total_cost *= weight
    return total_cost


def expand_node(node):
    # Find 0, which denotes the empty space
    matrix = node.curr_state
    space_r = 0
    space_c = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "0":
                space_r = r
                space_c = c

    children_list = []

    if space_r != len(matrix) - 1:
        child_matrix = [row[:] for row in matrix]
        child_matrix[space_r][space_c], child_matrix[space_r + 1][space_c] = child_matrix[space_r + 1][space_c], \
                                                                             child_matrix[space_r][space_c]
        child = Node(child_matrix, node, 0, "D", node.depth + 1)
        child.cost = find_weighted_cost(child, (space_r, space_c))
        children_list.append(child)

    if space_r > 0:
        child_matrix = [row[:] for row in matrix]
        child_matrix[space_r][space_c], child_matrix[space_r - 1][space_c] = child_matrix[space_r - 1][space_c], \
                                                                             child_matrix[space_r][space_c]
        child = Node(child_matrix, node, 0, "U", node.depth + 1)
        child.cost = find_weighted_cost(child, (space_r, space_c))
        children_list.append(child)

    if space_c != len(matrix[0]) - 1:
        child_matrix = [row[:] for row in matrix]
        child_matrix[space_r][space_c], child_matrix[space_r][space_c + 1] = child_matrix[space_r][space_c + 1], \
                                                                             child_matrix[space_r][space_c]
        child = Node(child_matrix, node, 0, "R", node.depth + 1)
        child.cost = find_weighted_cost(child, (space_r, space_c))
        children_list.append(child)

    if space_c > 0:
        child_matrix = [row[:] for row in matrix]
        child_matrix[space_r][space_c], child_matrix[space_r][space_c - 1] = child_matrix[space_r][space_c - 1], \
                                                                             child_matrix[space_r][space_c]
        child = Node(child_matrix, node, 0, "L", node.depth + 1)
        child.cost = find_weighted_cost(child, (space_r, space_c))
        children_list.append(child)
    return children_list

# From the node, find an array of the solution path and function costs
def find_solution_path(node):
    ans = [None] * node.depth
    ptr = len(ans) - 1
    while node.prev_action:
        ans[ptr] = node.prev_action
        node = node.parent
        ptr -= 1
    return ans


# From the goal node, return an array of the function costs
def find_function_costs(node):
    ans = [None] * (node.depth + 1)
    ptr = len(ans) - 1
    while node:
        ans[ptr] = node.curr_state
        node = node.parent
        ptr -= 1
    return ans

# Writes the solution to an output file, output.txt
def write_solution_to_file(original, depth, total_nodes, string_of_actions, A_costs_string):
    text_file = open("output.txt", "w")
    for row in original:
        for elem in row:
            text_file.write(str(elem) + " ")
        text_file.write("\n")
    text_file.write("\n")
    for row in goal:
        for elem in row:
            text_file.write(str(elem) + " ")
        text_file.write("\n")
    text_file.write("\n" + weight + "\n" + depth + "\n" + total_nodes + "\n")
    for elem in string_of_actions:
        text_file.write(str(elem) + " ")
    text_file.write("\n")
    for elem in A_costs_string:
        text_file.write(str(elem) + " ")
    text_file.close()
    return

# Reads the file, returns (start, goal, weight)
def read_file(file_name):
    start = [[0] * 4 for i in range(4)]
    data = ""

    # Reads the entire file into data
    with open(file_name) as file:
        data = file.read()

    # Removes all trailing spaces from data
    temp_data = []
    for i in range(len(data.split("\n"))):
        temp_data.append(data.split("\n")[i].rstrip())
    data = "\n".join(temp_data)

    # Splits data by empty line
    split_data = data.split("\n\n")

    # Weight is the first thing in the file
    global weight
    weight = float(split_data[0])

    # Start is the 2nd
    # Splits it by new line, then by space
    # Puts it all into start matrix
    start_rows = split_data[1].split("\n")
    for r in range(len(start_rows)):
        start_col = start_rows[r].split(" ")
        for c in range(len(start_col)):
            start[r][c] = start_col[c]

    # Goal is the 3rd
    # Splits it by new line, then by space
    # Puts it all into goal matrix
    goal_rows = split_data[2].split("\n")
    for r in range(len(goal_rows)):
        goal_col = goal_rows[r].split(" ")
        for c in range(len(goal_col)):
            goal[r][c] = goal_col[c]

    print("Start:", start)
    print("Goal:", goal)
    print("Weight:", weight)

    return start

# def main():
#     list1 = []
#     list1.append([1,2,3])
#     list1.append([4,5,6])
#     list1.append([7,8,9])
#     write_solution_to_file(list1, list1, "c", "d", "e", [1,2,3], ["a","b","c","d"]) # IT WORKS

def main():
    start = read_file("Input2.txt")
    result = a_star_algorithm(start)
    print(goal, weight)
    print("Goal:", goal)
    print("Weight:", weight)
    if result == "FAILURE":
        print("There is no solution")
        return
    write_solution_to_file(start, result[0], find_solution_path(result[1]), find_function_costs(result[1]))

if __name__ == "__main__":
    main()
