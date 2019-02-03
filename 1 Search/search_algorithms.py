from tkinter import *
from tkinter import ttk
import numpy as np
import utils
import time

class AI_algorithms:
    def __init__(self, root):
        root.title("AI algorithms")
        root.geometry("500x500")
        root.resizable(width=False, height=False)
        self.create_canvas(420, 420)
        self.btn_frame = Frame(root)
        self.add_buttons()
        self.btn_frame.pack()
        self.start = (0, 0)
        self.goal = (20, 20)
        self.arr = np.zeros((21, 21))
        self.arr[self.start[0], self.start[1]] = 1
        self.arr[self.goal[0], self.goal[1]] = 2
        self.print_canvas()

    def fill_canvas(self, event=None):
        print("Fill button clicked! The value of The dropdown is : ", self.var_alg.get())
        self.clear_canvas()
        if self.var_alg.get() == 'DFS':
            path = self.depthFirstSearch()
        else:
            path = self.breadthFirstSearch()
        self.print_canvas(path)


    def clear_canvas(self, event=None):
        self.drawing_area.create_rectangle(0, 0, self.c_width, self.c_height, fill="black")
        self.reset_arr()
        self.print_canvas()
        print("Cleared")

    def check_canvas(self, event=None):
        print("Check button clicked")

    def create_canvas(self, width, height):
        self.c_width = width
        self.c_height = height
        self.drawing_area = Canvas(root,
                                   width=self.c_width,
                                   height=self.c_height,
                                   bg="black")
        self.drawing_area.pack()

    def add_buttons(self):
        self.b_fill = ttk.Button(self.btn_frame, text="Fill", command=self.fill_canvas)
        self.b_clear = ttk.Button(self.btn_frame, text="Clear", command=self.clear_canvas)
        self.b_check = ttk.Button(self.btn_frame, text="Check", command=self.check_canvas)
        self.var_alg = StringVar(root)
        self.var_alg.set("DFS")
        self.options_menu = ttk.OptionMenu(self.btn_frame, self.var_alg, "DFS", "DFS", "BFS", "UCS", "A*")
        self.b_fill.pack(side=LEFT)
        self.b_clear.pack(side=LEFT)
        self.b_check.pack(side=LEFT)
        self.options_menu.pack(side=LEFT)

    def reset_arr(self):
        self.arr = np.zeros((21, 21))
        self.arr[self.start[0], self.start[1]] = 1
        self.arr[self.goal[0], self.goal[1]] = 2

    def print_canvas(self, path=[]):
        start_x = 20 * self.start[1]
        start_y = 20 * self.start[0]
        end_x = 20 * (self.start[1] + 1)
        end_y = 20 * (self.start[0] + 1)
        self.drawing_area.create_rectangle(start_x, start_y, end_x, end_y, fill="blue")
        start_x = 20 * self.goal[1]
        start_y = 20 * self.goal[0]
        end_x = 20 * (self.goal[1] + 1)
        end_y = 20 * (self.goal[0] + 1)
        self.drawing_area.create_rectangle(start_x, start_y, end_x, end_y, fill="green")

        rows, cols = self.arr.shape
        for i, j in path:
            start_x = 20 * j + 5
            start_y = 20 * i + 5
            end_x = 20 * (j + 1) - 5
            end_y = 20 * (i + 1) - 5
            self.drawing_area.create_oval(start_x, start_y, end_x, end_y, fill="red")

    ##Algorithms
    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        if state == self.goal:
            return True
        else:
            return False

    def getSuccessors(self, state):
        r, c = state
        suc = []
        #left
        if c > 0:
            cl = c - 1
            s_left = (r, cl)
            suc.append((s_left, [s_left], 0))

        #right
        if c < 20:
            cr = c + 1
            s_right = (r, cr)
            suc.append((s_right, [s_right], 0))

        #top
        if r > 0:
            rt = r - 1
            s_top = (rt, c)
            suc.append((s_top, [s_top], 0))

        #bottom
        if r < 20:
            rt = r + 1
            s_bot = (rt, c)
            suc.append((s_bot, [s_bot], 0))

        return suc

    def update_visited(self, state):
        i, j = state
        start_x = 20 * j + 5
        start_y = 20 * i + 5
        end_x = 20 * (j + 1) - 5
        end_y = 20 * (i + 1) - 5
        self.drawing_area.create_oval(start_x, start_y, end_x, end_y, fill="gray")
        self.drawing_area.update()
        time.sleep(0.01)

    def mark_visited(self, state):
        r, c = state
        self.arr[r, c] = -1
        self.update_visited(state)


    def depthFirstSearch(self):
        fringe = utils.Stack()
        start = self.getStartState()
        fringe.push((start, [], 0))
        visited = set([])
        while (fringe.isEmpty() == False):
            state, path, cost = fringe.pop()
            if state not in visited:
                visited.add(state)
                if self.isGoalState(state):
                    print(state, "Found GOAL")
                    print(path)
                    return path
                else:
                    for suc in self.getSuccessors(state):
                        suc_state, suc_dir, suc_cost = suc
                        fringe.push((suc_state, path + suc_dir, 0))
                self.mark_visited(state)
        return []

    def breadthFirstSearch(self):
        fringe = utils.Queue()
        start = self.getStartState()
        fringe.push((start, [], 0))
        visited = set([])
        while (fringe.isEmpty() == False):
            state, path, cost = fringe.pop()
            if state not in visited:
                visited.add(state)
                if self.isGoalState(state):
                    print(state, "Found GOAL")
                    print(path)
                    return path
                else:
                    for suc in self.getSuccessors(state):
                        suc_state, suc_dir, suc_cost = suc
                        fringe.push((suc_state, path + suc_dir, 0))
                self.mark_visited(state)
        return []


root = Tk();
app = AI_algorithms(root)
root.mainloop()