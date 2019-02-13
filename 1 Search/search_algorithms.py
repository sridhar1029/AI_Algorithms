import tkinter as tk
from tkinter import ttk
import numpy as np
from utils import *
import time

class AI_algorithms:
    def __init__(self, root):
        root.title("AI algorithms")
        root.geometry("500x520")
        root.resizable(width=False, height=False)
        self.title_var = tk.StringVar(root)
        self.title_var.set("Search Simulation")
        title_app = tk.Label(root, textvariable=self.title_var, font=("Tahoma", 25, 'bold'))
        title_app.pack(side=tk.TOP, fill=tk.X)
        self.create_canvas(420, 420)
        self.add_labels()
        self.btn_frame = ttk.Frame(root)
        self.add_buttons()
        self.btn_frame.pack()
        self.start = (3, 12)
        self.goal = (20, 20)
        self.reset_arr()
        self.print_canvas()

    def add_labels(self):
        self.cost_var = tk.IntVar(root)
        self.cost_var.set(0)
        self.expanded_count = tk.IntVar(root)
        self.expanded_count.set(0)
        cost_lbl = tk.Label(root, text="Path Cost : ", font=("Tahoma", 10))
        cost_label = tk.Label(root, textvariable=self.cost_var, font=("Tahoma", 10))
        cost_lbl.pack(side=tk.LEFT, fill=tk.X)
        cost_label.pack(side=tk.LEFT, fill=tk.X)
        cexp_lbl = tk.Label(root, text="Nodes Expanded : ", font=("Tahoma", 10))
        cexp_label = tk.Label(root, textvariable=self.expanded_count, font=("Tahoma", 10))
        cexp_label.pack(side=tk.RIGHT, fill=tk.X)
        cexp_lbl.pack(side=tk.RIGHT, fill=tk.X)

    def fill_canvas(self, event=None):
        print("Fill button clicked! The value of The dropdown is : ", self.var_alg.get())
        self.clear_canvas()
        if self.var_alg.get() == 'DFS':
            path = self.depthFirstSearch()
        elif self.var_alg.get() == 'BFS':
            path = self.breadthFirstSearch()
        elif self.var_alg.get() == 'UCS':
            path = self.uniformCostSearch()
        else:
            path = self.aStarSearch()
        self.print_canvas(path)


    def clear_canvas(self, event=None):
        self.drawing_area.create_rectangle(0, 0, self.c_width, self.c_height, fill="white")
        self.reset_arr()
        self.print_canvas()
        self.cost_var.set(0)
        self.expanded_count.set(0)
        print("Cleared")

    def create_canvas(self, width, height):
        self.c_width = width
        self.c_height = height
        self.drawing_area = tk.Canvas(root,
                                   width=self.c_width,
                                   height=self.c_height,
                                   bg="white")
        self.drawing_area.pack()

    def add_buttons(self):
        self.b_fill = ttk.Button(self.btn_frame, text="Search Goal", command=self.fill_canvas)
        self.b_clear = ttk.Button(self.btn_frame, text="Clear", command=self.clear_canvas)
        self.var_alg = tk.StringVar(root)
        self.var_alg.set("DFS")
        self.options_menu = ttk.OptionMenu(self.btn_frame, self.var_alg, "DFS", "DFS", "BFS", "UCS", "A*")
        self.b_fill.pack(side=tk.LEFT)
        self.b_clear.pack(side=tk.LEFT)
        self.options_menu.pack(side=tk.LEFT)

    def reset_arr(self):
        self.arr = np.copy(search_space)
        self.arr[self.start[0], self.start[1]] = 0
        self.arr[self.goal[0], self.goal[1]] = 0

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

        if path == []:
            rows, cols = self.arr.shape
            colors_arr = ["#000000", "#002730", "#013e4c", "#01657c", "#00a1c6"]
            for i in range(rows):
                for j in range(cols):
                    if (i, j) != self.start and (i, j) != self.goal:
                        ind = int(self.arr[i][j])
                        start_x = 20 * j
                        start_y = 20 * i
                        end_x = 20 * (j + 1)
                        end_y = 20 * (i + 1)
                        self.drawing_area.create_rectangle(start_x, start_y, end_x, end_y, fill=colors_arr[ind])


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
            suc.append((s_left, [s_left], int(self.arr[r][cl]) + 1))

        #right
        if c < 20:
            cr = c + 1
            s_right = (r, cr)
            suc.append((s_right, [s_right], int(self.arr[r][cr]) + 1))

        #top
        if r > 0:
            rt = r - 1
            s_top = (rt, c)
            suc.append((s_top, [s_top], int(self.arr[rt][c]) + 1))

        #bottom
        if r < 20:
            rb = r + 1
            s_bot = (rb, c)
            suc.append((s_bot, [s_bot], int(self.arr[rb][c]) + 1))

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
        fringe = Stack()
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
                    print(cost)
                    self.expanded_count.set(len(visited))
                    self.cost_var.set(cost)
                    return path
                else:
                    for suc in self.getSuccessors(state):
                        suc_state, suc_dir, suc_cost = suc
                        fringe.push((suc_state, path + suc_dir, cost + suc_cost))
                self.mark_visited(state)
        return []

    def breadthFirstSearch(self):
        fringe = Queue()
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
                    print(cost)
                    self.expanded_count.set(len(visited))
                    self.cost_var.set(cost)
                    return path
                else:
                    for suc in self.getSuccessors(state):
                        suc_state, suc_dir, suc_cost = suc
                        fringe.push((suc_state, path + suc_dir, cost + suc_cost))
                self.mark_visited(state)
        return []

    def uniformCostSearch(self):
        print("Starting UCS")
        fringe = PriorityQueue()
        start = self.getStartState()
        fringe.push((start, [], 0), 0)
        visited = set([])
        while(fringe.isEmpty() == False):
            state, path, cost = fringe.pop()
            if state not in visited:
                visited.add(state)
                if self.isGoalState(state):
                    print(state, "Found GOAL")
                    print(path)
                    print(cost)
                    self.expanded_count.set(len(visited))
                    self.cost_var.set(cost)
                    return path
                else:
                    for suc in self.getSuccessors(state):
                        suc_state, suc_dir, suc_cost = suc
                        fringe.push((suc_state, path + suc_dir, cost + suc_cost), cost + suc_cost)
                self.mark_visited(state)
        return []

    def manhattanDist(self, state):
        dis = np.abs(state[0] - self.goal[0]) + np.abs(state[1] - self.goal[1])
        return dis

    def aStarSearch(self, heuristic=None):
        if heuristic == None:
            heuristic = self.manhattanDist
        fringe = PriorityQueue()
        start = self.getStartState()
        fringe.push((start, [], 0), 0 + heuristic(start))
        visited = set([])
        while (fringe.isEmpty() == False):
            state, path, cost = fringe.pop()
            if state not in visited:
                visited.add(state)
                if self.isGoalState(state):
                    print(state, "Found GOAL")
                    print(path)
                    print(cost)
                    self.expanded_count.set(len(visited))
                    self.cost_var.set(cost)
                    return path
                else:
                    for suc in self.getSuccessors(state):
                        suc_state, suc_dir, suc_cost = suc
                        cum_cost = cost + suc_cost
                        f = cum_cost + heuristic(suc_state)
                        fringe.push((suc_state, path + suc_dir, cum_cost), f)
                self.mark_visited(state)
        return []


root = tk.Tk()
app = AI_algorithms(root)
root.mainloop()