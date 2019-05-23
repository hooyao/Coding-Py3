#!/usr/bin/env python  
""" 
@author:shz 
@license: Apache Licence 
@file: dijkstra.py 
@time: 2019/05/23
@contact: sunhouzan@163.com
@site:  
@software: PyCharm 
"""
import heapq
import sys
from typing import List, Dict


class Edge:
    from_id: int
    to_id: int
    weight: int

    def __init__(self, fid: int, tid: int, weight: int) -> None:
        super().__init__()
        self.from_id = fid
        self.to_id = tid
        self.weight = weight

    def __repr__(self) -> str:
        return f'from:{self.from_id}  to:{self.to_id} W:{self.weight}'


class Graph:
    adj = Dict[int, List[Edge]]
    vertex_count: int


class Dijkstra:

    def search(self, graph: Graph, from_id: int, to_id: int):
        distance = {}
        priority_queue = []
        inqueue = {}
        for i in range(graph.vertex_count):
            distance[i] = sys.maxsize
            inqueue[i] = False
        distance[from_id] = 0
        inqueue[from_id] = True
        heapq.heappush(priority_queue, (distance[from_id], from_id))
        while len(priority_queue) > 0:
            (min_distance, min_vertex_id) = heapq.heappop(priority_queue)
            if min_vertex_id == to_id:
                break
            for edge in graph.adj[min_vertex_id]:
                if edge.weight + min_distance < distance[edge.to_id]:
                    distance[edge.to_id] = edge.weight + min_distance
                    if inqueue[edge.to_id]:
                        # update priority_queue
                        for idx, item in enumerate(priority_queue):
                            if item[1] == edge.to_id:
                                priority_queue.pop(idx)
                                break
                        heapq.heappush(priority_queue, (distance[edge.to_id], edge.to_id))
                    else:
                        heapq.heappush(priority_queue, (distance[edge.to_id], edge.to_id))
                        inqueue[edge.to_id] = True
        return distance[to_id]


def main(*args):
    graph = Graph()
    graph.vertex_count = 5
    adj = dict()
    adj_0 = [Edge(0, 1, 1), Edge(0, 2, 5)]
    adj_1 = [Edge(1, 3, 2)]
    adj_2 = [Edge(2, 1, 1), Edge(2, 4, 2)]
    adj_3 = [Edge(3, 2, 1), Edge(3, 4, 2)]
    adj_4 = []
    adj[0] = adj_0
    adj[1] = adj_1
    adj[2] = adj_2
    adj[3] = adj_3
    adj[4] = adj_4
    graph.adj = adj
    shortest_length = Dijkstra().search(graph, 0, 4)
    print(shortest_length)


if __name__ == '__main__':
    main(*sys.argv[1:])
