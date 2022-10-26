'''
Project 1:
A* Algorithm for the 15-Puzzle Problem
Steven Han and Preston Tang
CS 4613
'''

import heapq



def a_star_algorithm(start, goal, weight):
    # Each node should have a tuple of its f(n), and its resulting board state
    frontier = heapq()
    # key is the state, and the value is the lowest path cost
    reached = dict()
    frontier.put((find_weighted_cost(start,), start))
    while len(frontier):
        # Each node should have a priority value calculated from our weighted A*, and the resulting board state
        node = frontier.pop()
        if(node == goal):
            return node
        for (weighted_cost, curr_state) in expand_node(node[1], node):
            if curr_state not in reached or weighted_cost < reached[curr_state]:
                reached[curr_state] = weighted_cost
                frontier.push(weighted_cost, curr_state)
    # If no solution
    return "FAILURE"


def find_weighted_cost(curr_matrix, weight):
    # For Preston
    # Find the full cost of the mann dist*weight + path cost 
    return 0

def expand_node(curr_matrix, node):
    #PRESTON'S
    # Should return a tuple with the full cost and the resulting board state
    pass

def read_file(file_name):
    #PRESTON YOU GOT THIS!!!
    # read the file, and return start, goal, and weight
    pass

# Writes the solution to an output file, output.txt
def write_solution_to_file(original, goal, weight, depth, total_nodes, string_of_actions, A_costs_string):
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

# def main():
#     list1 = []
#     list1.append([1,2,3])
#     list1.append([4,5,6])
#     list1.append([7,8,9])
#     write_solution_to_file(list1, list1, "c", "d", "e", [1,2,3], ["a","b","c","d"]) # IT WORKS

def main():
    return

if __name__ == "__main__":
    main()