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
    write_to_file = ""
    for row in original:
        write_to_file += str(row) + "\n"
    write_to_file += "\n"
    for row in goal:
        write_to_file += str(row) + "\n"
    write_to_file += "\n" + weight + "\n" + depth + "\n" + total_nodes + "\n"
    write_to_file += string_of_actions + "\n" + A_costs_string 
    #Turn string into file
    text_file = open("D:/data.txt", "w")
    text_file.write(write_to_file)
    text_file.close()
    return

def main():
    list1 = []
    list1.append([1,2,3])
    list1.append([4,5,6])
    list1.append([7,8,9])
    write_solution_to_file(list1, list1, "c", "d", "e", [1,2,3], ["a","b","c","d"]) # Crying cause it don't work rn T_T

if __name__ == "__main__":
    main()