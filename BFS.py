import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets as qtw


class BFS:
    array_gui = []

    def solve(start, goal):
        BFS.array_gui.clear()
        begin = time.time()
        depth = start.depth
        frontier_s = set()
        frontier_q = []
        explored = set()
        parent_map = {}
        frontier_s.add(start)
        frontier_q.append(start)
        while frontier_s:
            s = frontier_q.pop(0)
            frontier_s.remove(s)
            v = s.value
            explored.add(s)
            depth = max(depth, s.depth)            
            if s == goal:
                print("Goal achieved")
                print(v)
                break
            array = s.children()            
            for child in array:
                if child not in explored and child not in frontier_s:
                    frontier_s.add(child)
                    frontier_q.append(child)
                    parent_map[child] = s
                    parent_map[child] = s
        end = time.time()
        print("Depth ", depth)
        print("Expanded ", len(explored))
        print(f"Total runtime of the BFS is {end - begin}")
        if s != goal:
            print("Goal not found")
            return
        BFS.path(parent_map, start, s)

    def path(parent_map, start, goal):
        path_a = []
        parent = goal
        cost = 0
        while parent != start:
            BFS.array_gui.append(parent.value)
            path_a.append(parent.value)
            parent = parent_map.get(parent)
        print("Cost", goal.cost)
        print("Cost:", len(path_a))
        path_a.reverse()
        BFS.array_gui.reverse()
        print(path_a)





