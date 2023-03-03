from PyQt5 import QtWidgets as qtw
import time
import Puzzle
from BFS import *
from DFS import *
from Astar import *
import main
from Puzzle import Ui_Dialog

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class BoardWindow(qtw.QDialog):
    array=[]
    start_val = 125340678
    goal_val = 12345678
    count = 0

    def __init__(self):
        super().__init__()
        self.puzzle = Ui_Dialog()
        self.puzzle.setupUi(self)
        self.puzzle.bfs.clicked.connect(self.solve_BFS)
        self.puzzle.dfs.clicked.connect(self.solve_DFS)
        self.puzzle.astarM.clicked.connect(self.solve_Astar_M)
        self.puzzle.astarE.clicked.connect(self.solve_Astar_E)
        self.puzzle.next.clicked.connect(self.get_next)
        self.puzzle.back.clicked.connect(self.get_back)
        self.puzzle.label.setStyleSheet("background-color: rgb(201, 217, 207);\n"
"font: 9pt \"RomanD\";")
 

    def get_digit(number, n):
        return number // 10 ** n % 10

    def print_state(self, state):
        if BoardWindow.get_digit(state, 2) == 0:
            self.puzzle.pushButton_8.setText("")
            self.puzzle.pushButton_8.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_8.setText(str(BoardWindow.get_digit(state, 2)))
            self.puzzle.pushButton_8.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")

        if BoardWindow.get_digit(state, 7) == 0:
            self.puzzle.pushButton_3.setText("")
            self.puzzle.pushButton_3.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_3.setText(str(BoardWindow.get_digit(state, 7)))
            self.puzzle.pushButton_3.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 6) == 0:
            self.puzzle.pushButton_2.setText("")
            self.puzzle.pushButton_2.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_2.setText(str(BoardWindow.get_digit(state, 6)))
            self.puzzle.pushButton_2.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 5) == 0:
            self.puzzle.pushButton_5.setText("")
            self.puzzle.pushButton_5.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_5.setText(str(BoardWindow.get_digit(state, 5)))
            self.puzzle.pushButton_5.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 4) == 0:
            self.puzzle.pushButton_6.setText("")
            self.puzzle.pushButton_6.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_6.setText(str(BoardWindow.get_digit(state, 4)))
            self.puzzle.pushButton_6.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 3) == 0:
            self.puzzle.pushButton_4.setText("")
            self.puzzle.pushButton_4.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_4.setText(str(BoardWindow.get_digit(state, 3)))
            self.puzzle.pushButton_4.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 1) == 0:
            self.puzzle.pushButton_9.setText("")
            self.puzzle.pushButton_9.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_9.setText(str(BoardWindow.get_digit(state, 1)))
            self.puzzle.pushButton_9.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 0) == 0:
            self.puzzle.pushButton_7.setText("")
            self.puzzle.pushButton_7.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton_7.setText(str(BoardWindow.get_digit(state, 0)))
            self.puzzle.pushButton_7.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")
        if BoardWindow.get_digit(state, 8) == 0:
            self.puzzle.pushButton.setText("")
            self.puzzle.pushButton.setStyleSheet("background-color: rgb(36, 52, 71);")
        else:
            self.puzzle.pushButton.setText(str(BoardWindow.get_digit(state, 8)))
            self.puzzle.pushButton.setStyleSheet("background-color: rgb(201, 217, 207);\n""font: 24pt \"RomanD\";")


    def solve_BFS(self):
        self.array.clear()
        BoardWindow.count = 0
        start = main.State(None, None, self.start_val, 0, 0, -1)
        goal = main.State(None, None, self.goal_val, 1, 0, -1)
        print("BFS")
        if self.puzzle.bfs:
            BoardWindow.print_state(self, self.start_val)
            BFS.solve(start, goal)
            print(BFS.array_gui)
            self.array=BFS.array_gui.copy()
            self.array.insert(0,self.start_val)
            print(self.array)
            self.puzzle.label.setText(" "+str(BoardWindow.count) + " out of " + str(len(self.array)-1))

    def solve_DFS(self):
        self.array.clear()
        BoardWindow.count = 0
        start = main.State(None, None, self.start_val, 0, 0, -1)
        goal = main.State(None, None, self.goal_val, 1, 0, -1)
        print("DFS")
        if self.puzzle.bfs:
            BoardWindow.print_state(self, self.start_val)
            DFS.solve(start, goal)
            print(DFS.array_gui)
            self.array=DFS.array_gui.copy()
            self.array.insert(0,self.start_val)
            #set label to 0 out of length of array
            self.puzzle.label.setText(" "+str(BoardWindow.count) + " out of " + str(len(self.array)-1))
    
    def solve_Astar_M(self):
        self.array.clear()
        BoardWindow.count = 0
        start = main.State(None, None, self.start_val, 0, 0, -1)
        goal = main.State(None, None, self.goal_val, 1, 0, -1)
        print("Astar Manhattan")
        if self.puzzle.bfs:
            BoardWindow.print_state(self, self.start_val)
            Astar.solve(start, goal, "M")
            print(Astar.array_gui)
            self.array=Astar.array_gui.copy()
            self.array.insert(0,self.start_val)
            self.puzzle.label.setText(" "+str(BoardWindow.count) + " out of " + str(len(self.array)-1))

    def solve_Astar_E(self):
        self.array.clear()
        BoardWindow.count = 0
        start = main.State(None, None, self.start_val, 0, 0, -1)
        goal = main.State(None, None, self.goal_val, 1, 0, -1)
        print("Astar Euclidean")
        if self.puzzle.bfs:
            BoardWindow.print_state(self, self.start_val)
            Astar.solve(start, goal, "E")
            print(BFS.array_gui)
            self.array=Astar.array_gui.copy()
            self.array.insert(0,self.start_val)
            self.puzzle.label.setText(" "+str(BoardWindow.count) + " out of " + str(len(self.array)-1))
    

    def get_next(self):
        # check which algorithm is selected
        if len(self.array) == 0:
            return
        if BoardWindow.count < len(self.array)-1:
            BoardWindow.count += 1
            BoardWindow.print_state(self, self.array[BoardWindow.count])
            self.puzzle.label.setText(str(BoardWindow.count) + " out of " + str(len(self.array)-1))
        else:
            msg = qtw.QMessageBox()
            msg.setText("No more moves")
            msg.setWindowTitle("Message")
            msg.exec_()
            BoardWindow.count = 0
            BoardWindow.print_state(self, self.array[BoardWindow.count])
            self.puzzle.label.setText(str(BoardWindow.count) + " out of " + str(len(self.array)-1))
            BoardWindow.count += 1

    def get_back(self):
        if len(self.array) == 0:
            return
        if BoardWindow.count > 0 :
            BoardWindow.count -= 1
            BoardWindow.print_state(self, self.array[BoardWindow.count])
            self.puzzle.label.setText(str(BoardWindow.count) + " out of " + str(len(self.array)-1))
        else:
            msg = qtw.QMessageBox()
            msg.setText("You are at the beginning")
            msg.setWindowTitle("Message")
            msg.exec_()



    def textbuttons(self):
        self.puzzle.pushButton.setText(("Dialog", "0"))
        self.puzzle.pushButton_2.setText(("Dialog", "1"))
        self.puzzle.pushButton_3.setText(("Dialog", "2"))
        self.puzzle.pushButton_4.setText(("Dialog", "3"))
        self.puzzle.pushButton_5.setText(("Dialog", "3"))
        self.puzzle.pushButton_6.setText(("Dialog", "4"))
        self.puzzle.pushButton_7.setText(("Dialog", "7"))
        self.puzzle.pushButton_8.setText(("Dialog", "2"))
        self.puzzle.pushButton_9.setText(("Dialog", "1"))


if __name__ == "__main__":
    import sys

    board = qtw.QApplication(sys.argv)
    gui = BoardWindow()
    start = 12345678
    gui.print_state(start)
    gui.show()
    #gui.solve()
    #gui.show()
    sys.exit(board.exec())
