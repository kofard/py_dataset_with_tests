from collections import deque
from math import floor
from random import random
from time import time

class DirectedGraph:

    def __init__(self) -> None:
        self.graph = {}

    def add_pair(self, u, v, w=1) -> None:
        """Adds a directed edge u->v with weight w.
        Add vertices and edges
        Add the weight is optional
        Handle repetition"""
        if self.graph.get(u):
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if not self.graph.get(v):
            self.graph[v] = []

    def all_nodes(self):
        """Returns list of all nodes in the graph."""
        return list(self.graph)

    def remove_pair(self, u, v) -> None:
        """Removes all edges u->v if it exists."""
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)

    def dfs(self, s=-2, d=-1):
        """Performs depth first search from s to find d.
        Returns the path s->d as a list.
        Returns dfs from s if d is not found"""
        stack = []
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []
        stack.append(s)
        while len(stack) > 0:
            s = stack.pop()
            visited.append(s)
            if s == d:
                break
            for _, ss in self.graph[s]:
                if visited.count(ss) < 1:
                    stack.append(ss)
        return visited

    def fill_graph_randomly(self, c=-1) -> None:
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.add_pair(i, n, 1)

    def bfs(self, s=-2):
        """Performs breadth first search from s
        Returns list."""
        d = deque()
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []
        d.append(s)
        visited.append(s)
        while d:
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        return visited

    def in_degree(self, u):
        count = 0
        for x in self.graph:
            for y in self.graph[x]:
                if y[1] == u:
                    count += 1
        return count

    def out_degree(self, u):
        return len(self.graph[u])

    def topological_sort(self, s=-2):
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s
        sorted_nodes = []
        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break
            if s == ss:
                sorted_nodes.append(stack.pop())
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss
            if len(stack) == 0:
                return sorted_nodes

    def cycle_nodes(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()
        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) > 0 and node[1] != parent and (indirect_parents.count(node[1]) > 0) and (not on_the_way_back):
                        len_stack = len(stack) - 1
                        while len_stack >= 0:
                            if stack[len_stack] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            anticipating_nodes.add(stack[len_stack])
                            len_stack -= 1
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss
            if len(stack) == 0:
                return list(anticipating_nodes)

    def has_cycle(self) -> bool | None:
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()
        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) > 0 and node[1] != parent and (indirect_parents.count(node[1]) > 0) and (not on_the_way_back):
                        len_stack_minus_one = len(stack) - 1
                        while len_stack_minus_one >= 0:
                            if stack[len_stack_minus_one] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss
            if len(stack) == 0:
                return False

    def dfs_time(self, s=-2, e=-1):
        begin = time()
        self.dfs(s, e)
        end = time()
        return end - begin

    def bfs_time(self, s=-2):
        begin = time()
        self.bfs(s)
        end = time()
        return end - begin

class Graph:

    def __init__(self) -> None:
        self.graph = {}

    def add_pair(self, u, v, w=1) -> None:
        if self.graph.get(u):
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if self.graph.get(v):
            if self.graph[v].count([w, u]) == 0:
                self.graph[v].append([w, u])
        else:
            self.graph[v] = [[w, u]]

    def remove_pair(self, u, v) -> None:
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)
        if self.graph.get(v):
            for _ in self.graph[v]:
                if _[1] == u:
                    self.graph[v].remove(_)

    def dfs(self, s=-2, d=-1):
        """Performs depth first search from s to find d.
        Returns the path s->d as a list.
        Returns dfs from s if d is not found"""
        stack = []
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []
        stack.append(s)
        while len(stack) > 0:
            s = stack.pop()
            if visited.count(s) == 1:
                continue
            visited.append(s)
            if s == d:
                break
            for _, ss in self.graph[s]:
                if visited.count(ss) < 1:
                    stack.append(ss)
        return visited

    def fill_graph_randomly(self, c=-1) -> None:
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.add_pair(i, n, 1)

    def bfs(self, s=-2):
        """Performs breadth first search from s
        Returns list."""
        d = deque()
        visited = []
        if s == -2:
            if self.graph.get(s, None):
                pass
            elif len(self.graph) > 0:
                s = next(iter(self.graph))
            else:
                return []
        d.append(s)
        visited.append(s)
        while d:
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        return visited

    def degree(self, u):
        return len(self.graph[u])

    def cycle_nodes(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()
        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) > 0 and node[1] != parent and (indirect_parents.count(node[1]) > 0) and (not on_the_way_back):
                        len_stack = len(stack) - 1
                        while len_stack >= 0:
                            if stack[len_stack] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            anticipating_nodes.add(stack[len_stack])
                            len_stack -= 1
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss
            if len(stack) == 0:
                return list(anticipating_nodes)

    def has_cycle(self) -> bool | None:
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()
        while True:
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) > 0 and node[1] != parent and (indirect_parents.count(node[1]) > 0) and (not on_the_way_back):
                        len_stack_minus_one = len(stack) - 1
                        while len_stack_minus_one >= 0:
                            if stack[len_stack_minus_one] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss
            if len(stack) == 0:
                return False

    def all_nodes(self):
        return list(self.graph)

    def dfs_time(self, s=-2, e=-1):
        begin = time()
        self.dfs(s, e)
        end = time()
        return end - begin

    def bfs_time(self, s=-2):
        begin = time()
        self.bfs(s)
        end = time()
        return end - begin