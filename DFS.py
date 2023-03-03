import time

from PyQt5 import QtCore, QtGui, QtWidgets
from main import State

class DFS:
    frontier_s = set()
    frontier_q = []
    array_gui = []

    def solve(start, goal):
        DFS.array_gui.clear()
        begin = time.time()
        frontier_s = set()
        frontier_q = []
        depth = start.depth
        explored = set()
        parent_map = {}
        frontier_s.add(start)
        frontier_q.append(start)
        while frontier_s:
            # remove x from frontier
            s = frontier_q.pop()
            frontier_s.remove(s)
            explored.add(s)
            depth = max(depth, s.depth)
            if s == goal:
                print("Goal achieved")
                break
            array = s.children()
            array.reverse()
            for child in array:
                if child not in explored and child not in frontier_s:
                    frontier_s.add(child)
                    frontier_q.append(child)
                    parent_map[child]=s
        end = time.time()
        print("Depth ", depth)
        print("Expanded ", len(explored))
        print(f"Total runtime of the DFS is {end - begin}")
        if s != goal:
            print("Goal not found")
            return
        DFS.path(parent_map, start, s)

    def path(parent_map, start, goal):
        path_a = []
        parent = goal
        cost = 0
        while parent != start:
            path_a.append(parent.action)
            DFS.array_gui.append(parent.value)
            parent = parent_map.get(parent)
        print("Cost", goal.cost)
        path_a.reverse()
        DFS.array_gui.reverse()
        print(path_a)
