'''
Project 1:
A* Algorithm for the 15-Puzzle Problem
Steven Han and Preston Tang
CS 4613
'''

import heapq

from numpy import string_


def a_star_algorithm(matrix, goal):
    frontier = heapq()
    # key is the state, and the value is the lowest path cost
    reached = dict()
    while len(frontier):
        node = frontier.pop()
        if(node == goal):
            return node
        for child in expand_node(node):
            s = child.state
            if s not in reached or child.path_cost < reached[s]:
                reached[s] = child
                frontier.push(child, child.path_cost)
    # If no solution
    return {{}}


def expand_node(problem, node):
    #PRESTON'S
    pass

def read_file(file_name):
    #PRESTON YOU GOT THIS!!!
    pass

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

def main():
    list1 = []
    list1.append([1,2,3])
    list1.append([4,5,6])
    list1.append([7,8,9])
    write_solution_to_file(list1, list1, "c", "d", "e", [1,2,3], ["a","b","c","d"]) # IT WORKS

if __name__ == "__main__":
    main()