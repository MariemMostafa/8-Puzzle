from queue import PriorityQueue
import time
import math
from PyQt5 import QtCore, QtGui, QtWidgets


class Astar:
    array_gui = []

    def solve(start, goal, mode):
        Astar.array_gui.clear()
        begin = time.time()
        if mode == "M":
            Astar.manhattan(start, goal)
        else:
            Astar.eucledian(start, goal)
        depth = start.depth
        frontier_h = PriorityQueue()
        frontier_s = set()
        explored = set()
        parent_map = {}
        depth = start.depth
        frontier_s.add(start)
        frontier_h.put(start)
        while frontier_s:
            s = frontier_h.get()
            if s in frontier_s:
                frontier_s.remove(s)
            else:
                continue
            v = s.value
            explored.add(s)
            depth = max(depth, s.depth)
            if s == goal:
                print("Goal Achieved")
                print(v)
                break
            array = s.children()
            for child in array:
                if child not in explored and child not in frontier_s:
                    if mode == "M":
                        Astar.manhattan(child, goal)
                    else:
                        Astar.eucledian(child, goal)
                    frontier_s.add(child)
                    frontier_h.put(child)
                    parent_map[child] = s
                    parent_map[child] = s
                elif child not in explored and child in frontier_s:
                    old_child = parent_map.get(child)
                    if old_child.f > child.f:
                        if old_child in frontier_s:
                            frontier_s.remove(old_child)
                        parent_map[child] = s
                        frontier_s.add(child)
                        frontier_h.put(child)
        end = time.time()
        print("Depth ", depth)
        print("Expanded ", len(explored))
        print(f"Total runtime of the Astar is {end - begin}")
        if s != goal:
            print("Goal not found")
            return
        Astar.path(parent_map, start, s)

    def manhattan(state_node, goal_node):
        h = 0
        state = state_node.value
        goal = goal_node.value
        goal_index = {}
        j = 0
        while goal != 0:
            goal_i = goal % 10
            goal_index[goal_i] = ((8 - j) % 3, (8 - j) // 3)
            goal = goal // 10
            j += 1
        for i in range(8):
            digit = state % 10
            if digit == 0:
                state = state // 10
                continue
            x_n = (8 - i) % 3
            x_g = (goal_index[digit])[0]
            y_n = (8 - i) // 3
            y_g = (goal_index[digit])[1]
            manhat = abs(x_n - x_g) + abs(y_n - y_g)
            h += manhat
            state = state // 10
        state_node.f = state_node.cost + h
        state_node.heuristic = h

    def eucledian(state_node, goal_node):
        h = 0
        state = state_node.value
        goal = goal_node.value
        goal_index = {}
        j = 0
        while goal != 0:
            goal_i = goal % 10
            goal_index[goal_i] = ((8 - j) % 3, (8 - j) // 3)
            goal = goal // 10
            j += 1
        for i in range(8):
            digit = state % 10
            if digit == 0:
                state = state // 10
                continue
            x_n = (8 - i) % 3
            x_g = (goal_index[digit])[0]
            y_n = (8 - i) // 3
            y_g = (goal_index[digit])[1]
            eucl = math.sqrt(abs(x_n - x_g) ** 2 + abs(y_n - y_g) ** 2)
            h += eucl
            state = state // 10
        state_node.heuristic = h

    def path(parent_map, start, goal):
        path_a = []
        parent = goal
        cost = 0
        while parent != start:
            path_a.append(parent.action)
            Astar.array_gui.append(parent.value)
            parent = parent_map.get(parent)
        print("Cost", goal.cost)
        path_a.reverse()
        Astar.array_gui.reverse()
        print(path_a)
