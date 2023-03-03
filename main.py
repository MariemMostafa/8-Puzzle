import sys


from BFS import *
from DFS import *
from Astar import *

from PyQt5 import QtCore, QtGui, QtWidgets
from Puzzle import Ui_Dialog


class State():
    array_gui = []

    def __init__(self, parent, action, value, cost, depth, heuristic):
        self.parent = parent
        self.action = action  # left,right,up,down
        self.value = value  #integer value of the whole board
        self.cost = cost
        self.depth = depth
        self.heuristic = heuristic
        self.f = heuristic+cost

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        return ((self.f, self.f) < (other.f, other.f))

    def children(self):
        children = []
        arr_children = []
        actions = ["left", "right", "down", "up"]
        puzzle = str(self.value)
        if len(puzzle) == 8:
            puzzle = '0' + puzzle
        p = puzzle.index('0')
        if p % 3 == 0:
            actions.remove("left")
        if p % 3 == 2:
            actions.remove("right")
        if p / 3 < 1:
            actions.remove("up")
        if p / 3 >= 2:
            actions.remove("down")
        for action in actions :
            clone = list(puzzle)
            if action == "down":
            # move down
                clone[p], clone[p + 3] = clone[p + 3], clone[p]
            if action == "up":
            # move up
                clone[p], clone[p - 3] = clone[p - 3], clone[p]
            if action == "left":
            # move left
                clone[p], clone[p - 1] = clone[p - 1], clone[p]
            if action == "right":
            # move right
                clone[p], clone[p + 1] = clone[p + 1], clone[p]
            children.append(State(self, action, int(''.join(clone)), self.cost+1, self.depth+1, -1))
        return children


class Board():
    def __init__(self, start , goal):
        self.start = start
        self.goal = goal


if __name__ == "__main__":
    start_val = 125340678
    goal_val = 12345678
    start = State(None, None, start_val, 0, 0, -1)
    goal = State(None, None, goal_val, 1, 0, -1)
    print("BFS")
    BFS.solve(start, goal)
    print("____________________________________________________________")
    print("DFS")
    DFS.solve(start, goal)
    print("____________________________________________________________")
    print("A-star Manhattan")
    Astar.solve(start, goal, "M")
    print("____________________________________________________________")
    print("A-star Eucledian")
    Astar.solve(start, goal, "E")
