import numpy as np
search_space = np.array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 2., 2., 2., 3., 4., 4., 4., 4., 4.],
                        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 2., 2., 2., 3., 3., 4., 4., 4., 4., 4.],
                        [1., 0., 1., 1., 1., 1., 1., 1., 2., 0., 0., 0., 0., 0., 0., 0., 0., 0., 4., 4., 4.],
                        [1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 3., 4., 4., 4., 0., 4., 4., 4.],
                        [1., 1., 0., 1., 1., 1., 1., 1., 2., 2., 2., 3., 0., 3., 4., 4., 4., 0., 4., 4., 4.],
                        [1., 1., 0., 0., 1., 1., 1., 1., 2., 2., 2., 3., 0., 3., 4., 4., 4., 0., 0., 0., 0.],
                        [1., 1., 1., 0., 1., 1., 1., 1., 2., 2., 2., 3., 0., 3., 4., 4., 4., 4., 4., 4., 4.],
                        [1., 1., 1., 0., 0., 1., 1., 1., 2., 2., 2., 3., 0., 3., 4., 4., 4., 4., 4., 4., 4.],
                        [1., 1., 1., 1., 0., 1., 1., 1., 2., 2., 2., 3., 0., 3., 4., 4., 4., 4., 4., 4., 4.],
                        [1., 1., 1., 1., 0., 0., 1., 1., 2., 2., 2., 3., 0., 3., 4., 4., 4., 4., 4., 4., 4.],
                        [2., 3., 3., 4., 4., 0., 0., 4., 4., 3., 3., 3., 0., 2., 2., 4., 4., 4., 4., 4., 4.],
                        [2., 3., 3., 4., 4., 4., 0., 4., 4., 3., 3., 3., 0., 2., 2., 2., 2., 4., 4., 4., 4.],
                        [2., 3., 3., 4., 4., 4., 0., 4., 4., 3., 3., 3., 0., 0., 0., 0., 1., 2., 4., 4., 4.],
                        [2., 3., 3., 4., 4., 4., 0., 4., 4., 3., 3., 3., 2., 2., 2., 0., 1., 2., 2., 2., 2.],
                        [2., 3., 3., 4., 4., 4., 0., 4., 4., 3., 3., 3., 2., 2., 2., 0., 1., 1., 2., 2., 2.],
                        [2., 3., 3., 4., 4., 4., 0., 4., 4., 3., 3., 3., 2., 2., 2., 0., 1., 1., 1., 2., 1.],
                        [2., 3., 3., 4., 4., 4., 0., 4., 4., 3., 3., 3., 2., 2., 2., 0., 0., 0., 0., 0., 0.],
                        [2., 3., 3., 4., 4., 4., 0., 0., 0., 0., 0., 3., 2., 2., 2., 1., 1., 1., 1., 2., 1.],
                        [2., 3., 3., 4., 4., 4., 4., 4., 4., 3., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
                        [2., 3., 3., 4., 4., 4., 4., 4., 4., 3., 3., 3., 2., 2., 2., 1., 1., 1., 1., 0., 0.],
                        [2., 3., 3., 4., 4., 4., 4., 4., 4., 3., 3., 3., 2., 2., 2., 1., 1., 1., 1., 2., 1.]])


class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

class Queue:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        return self.list.pop()

    def isEmpty(self):
        return len(self.list) == 0

class Heap:
    def __init__(self, lis=[]):
        self.list = [0]
        self.length = 0
        for el in lis:
            self.insert(el)

    def get_val(self, i):
        if i<=self.length and i>0:
            return self.list[i]
        return None

    def insert(self, val):
        self.list.append(val)
        self.length += 1

    def delete_item(self, i):
        popped = self.list.pop(i)
        self.length -= 1
        return popped

    def parent(self, i):
        if i <= self.length and i > 1:
            par = int(i/2)
            return (self.list[par], par)
        else:
            return None

    def left(self, i):
        if i <= self.length:
            child_l = 2*i
            if child_l <= self.length:
                return (self.list[child_l], child_l)
            return None
        else:
            return None

    def right(self, i):
        if i <= self.length:
            child_r = 2*i + 1
            if child_r <= self.length:
                return (self.list[child_r], child_r)
            return None
        else:
            return None

class MaxHeap(Heap):
    def __init__(self, lis=[]):
        super().__init__(lis)

    def get_max(self):
        return self.list[1]

    def extract_max(self):
        extracted = self.list[1]
        self.list[1] = self.list[self.length]
        self.list.pop(self.length)
        self.length -= 1
        self.max_heapify(1)
        return extracted

    def build_max_heap(self):
        for i in range(int(self.length/2), 0, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        par = self.get_val(i)
        child_l = self.left(i)
        child_r = self.right(i)
        if child_l == None and child_r == None:
            return
        elif child_l != None and child_r == None:
            if child_l[0] > par:
                self.list[i] = child_l[0]
                self.list[child_l[1]] = par
                self.max_heapify(child_l[1])
        elif child_r != None and child_l == None:
            if child_r[0] > par:
                self.list[i] = child_r[0]
                self.list[child_r[1]] = par
                self.max_heapify(child_r[1])
        else:
            if child_l[0] > child_r[0]:
                if child_l[0] > par:
                    self.list[i] = child_l[0]
                    self.list[child_l[1]] = par
                    self.max_heapify(child_l[1])
            else:
                if child_r[0] > par:
                    self.list[i] = child_r[0]
                    self.list[child_r[1]] = par
                    self.max_heapify(child_r[1])
        return

    def insert(self, val):
        super().insert(val)
        par = self.parent(self.length)
        while par != None:
            self.max_heapify(par[1])
            par = self.parent(par[1])

class MinHeap(Heap):
    def __init__(self, lis=[]):
        super().__init__(lis)

    def get_min(self):
        return self.list[1]

    def extract_min(self):
        extracted = self.list[1]
        self.list[1] = self.list[self.length]
        self.list.pop(self.length)
        self.length -= 1
        self.min_heapify(1)
        return extracted

    def build_min_heap(self):
        for i in range(int(self.length/2), 0, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        par = self.get_val(i)
        child_l = self.left(i)
        child_r = self.right(i)
        if child_l == None and child_r == None:
            return
        elif child_l != None and child_r == None:
            if child_l[0] < par:
                self.list[i] = child_l[0]
                self.list[child_l[1]] = par
                self.min_heapify(child_l[1])
        elif child_r != None and child_l == None:
            if child_r[0] < par:
                self.list[i] = child_r[0]
                self.list[child_r[1]] = par
                self.min_heapify(child_r[1])
        else:
            if child_l[0] < child_r[0]:
                if child_l[0] < par:
                    self.list[i] = child_l[0]
                    self.list[child_l[1]] = par
                    self.min_heapify(child_l[1])
            else:
                if child_r[0] < par:
                    self.list[i] = child_r[0]
                    self.list[child_r[1]] = par
                    self.min_heapify(child_r[1])
        return

    def insert(self, val):
        super().insert(val)
        par = self.parent(self.length)
        while par != None:
            self.min_heapify(par[1])
            par = self.parent(par[1])

class PriorityQueue(MinHeap):
    def push(self, item, priority=0):
        self.insert((priority, item))

    def pop(self):
        pop_it = self.extract_min()
        return pop_it[1]

    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False

    def update(self, item, priority):
        pass

class PriorityQueueWithFunction(PriorityQueue):
    def __init__(self, priority_function):
        super().__init__()
        self.priority_function = priority_function

    def push(self, item):
        priority = self.priority_function(item)
        self.insert((priority, item))