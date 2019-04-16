"""
Simple graph implementation
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def push(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None

    def len(self):
        return self.size


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = list()

    def enqueue(self, item):
        if item not in self.storage:
            self.storage.append(item)
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)
        return None

    def len(self):
        return self.size


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise IndexError("That vertex does not exist")

    def add_directed_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist, good sir!")

    # def bft(self, starting_vertex_id):
    #     q = Queue()
    #     q.enqueue(starting_vertex_id)
    #     visited = set()
    #     while q.size() > 0:
    #         vertex = q.dequeue()
    #         if vertex not in visited:
    #             visited.add(vertex)
    #             for next_vert in self.vertices[vertex]:
    #                 q.enqueue(next_vert)

    # def dft(self, starting_vertex_id):
    #     s = Stack()
    #     s.push(starting_vertex_id)
    #     visited = set()
    #     while s.size() > 0:
    #         vertex = s.pop()
    #         if vertex not in visited:
    #             print(vertex)
    #             visited.add(vertex)
    #             for next_vert in self.vertices[vertex]:
    #                 s.push(next_vert)

    # def dft_recursive(self, vertex, visited=None):
    #     if visited == None:
    #         visited = set()
    #     visited.add(vertex)
    #     for next_vert in self.vertices[vertex]:
    #         if next_vert not in visited:
    #             return self.dft_recursive(next_vert, visited)

    # def bfs(self, starting_vertex, target):
    #     queue = Queue()
    #     visited = set()
    #     queue.enqueue([starting_vertex])
    #     while queue.size() > 0:
    #         queue_check = queue.dequeue()
    #         if queue_check[-1] not in visited:
    #             visited.add(queue_check[-1])
    #             if queue_check[-1] == target:
    #                 return queue_check
    #             for next_vert in self.vertices[queue_check[-1]]:
    #                 path = queue_check[:]
    #                 path.append(next_vert)
    #                 queue_check.enqueue(path)

    def dfs(self, starting_vertex, target):
        s = Stack()
        visited = set()
        s.push([starting_vertex])
        while s.size() > 0:
            stack_to_check = s.pop()
            if stack_to_check[-1] not in visited:
                visited.add(stack_to_check[-1])
                if stack_to_check[-1] == target:
                    return stack_to_check
                for next_vert in self.vertices[stack_to_check[-1]]:
                    path = stack_to_check[:]
                    path.append(next_vert)
                    stack_to_check.enqueue(path)
